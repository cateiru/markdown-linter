'''
main.
'''
import os
import re
import sys
from typing import List
from urllib import error, request

from bs4 import BeautifulSoup

from src import md_error


class Analysis():
    '''
    Markdownを静的解析するクラス。
    '''

    def __init__(self, save_file_dir: str, file_path: str) -> None:
        self.save_file_dir = save_file_dir
        self.file_path = file_path

        self.body = Analysis.__read_md(self.file_path)
        self.new_file_name = None

    @staticmethod
    def __read_md(file_path: str) -> List[str]:
        '''
        ファイルパスからファイルの本文を読み込みます。

        Returns:
            List[str]: `.md`ファイルの本文。各行ごとにリストに分かれます。
        '''
        with open(file_path) as md_file:
            body_slice = md_file.read().split('\n')

        return body_slice

    def check_blank_line(self) -> None:
        '''
        文の末尾の空白行と連続した複数の空白行をチェックします。
        1. 末尾の空白行は1つのみです。なにもない、2個以上ある場合は1つにします。
        2. 連続した複数の空白行は1つの空白行に変更します。
        '''
        # Check the last line.
        blank_line = 1
        while self.body[-blank_line] == '':
            blank_line += 1
        if blank_line == 1:
            self.body.append('')
        elif blank_line > 1:
            del self.body[-(blank_line-1):]
            self.body.append('')

        # Two or more spaces.
        is_befor_blank_line = False
        count = 0
        more_blank_line = []
        for index, line in enumerate(self.body):
            if line == '':
                if is_befor_blank_line:
                    more_blank_line.append(index)
                is_befor_blank_line = True
            else:
                is_befor_blank_line = False

        for line_index in more_blank_line:
            del self.body[line_index-count]
            count += 1

    def check_title(self) -> str:
        '''
        Markdownのタイトルを整形します。
        1. `#`とタイトル文の間に空白を開けます。
        2. タイトルは一番トップレベルの行であり、その上には何もありません。
        3. タイトルの下の行は1つの空白行があります。

        Raises:
            TitleNotFound: Markdown内にタイトルが存在しない場合。
            FormatError: タイトル文の中に`#`が存在する場合。
            FormatError: タイトルが複数個存在する場合。

        Returns:
            str: タイトルの本文
        '''
        count_title = 0
        for index, line in enumerate(self.body):
            title = re.fullmatch(r'^\#\s?(?P<title>[^\#]+)(?P<invalid>(.+)?)', line)
            if title:
                if title.group('invalid'):
                    raise md_error.FormatError('`#` Exists in the body of the title.')
                title_body = title.group('title')
                title_line = index
                count_title += 1
        if count_title == 0:
            raise md_error.TitleNotFound('Title not found.')
        if count_title > 1:
            raise md_error.FormatError('Multiple titles.')

        self.body.insert(0, f'# {title_body}')
        del self.body[title_line+1]

        # add & remove blank line
        check_blank_line = 1
        while self.body[check_blank_line] == '':
            check_blank_line += 1
        if check_blank_line != 2:
            del self.body[1:check_blank_line]
            self.body.insert(1, '')

        return title_body

    def check_header(self) -> None:
        '''
        Markdownの全てのレベルのヘッダーを整形します。
        1. `#`とヘッダー文の間に空白を空けます。
        2. ヘッダーの上下の行は空白行でなければいけません。

        Raises:
            md_error.FormatError: ヘッダー文の中に`#`が存在する場合。
        '''
        headers = dict()
        header_level = 0
        header_level_befor = None
        for index, line in enumerate(self.body):
            header = re.fullmatch(r'^(?P<level>\#{2,})\s?(?P<header>[^\#]+)(?P<invalid>(.+)?)', line)
            if header:
                if header.group('invalid'):
                    raise md_error.FormatError('`#` Exists in the body of the header.')
                header_level = header.group('level').count('#')
                if header_level == header_level_befor or header_level+1 == header_level_befor or\
                        header_level-1 == header_level_befor or header_level_befor is None:
                    header_level_befor = header_level
                else:
                    raise md_error.FormatError('The header is incremented by one level at a time.')

                header_level_befor = header_level
                headers[index] = [header.group('header'), header.group('level')]

        blank_line_count = 0
        for line_index in headers:
            self.body[line_index+blank_line_count] = f'{headers[line_index][1]} {headers[line_index][0]}'

            check_blank_line_deep = 1
            check_blank_line_shallow = 1
            while self.body[line_index+check_blank_line_deep+blank_line_count] == '':
                check_blank_line_deep += 1
            while self.body[line_index-check_blank_line_shallow+blank_line_count] == '':
                check_blank_line_shallow += 1

            if check_blank_line_shallow != 2:
                del self.body[line_index-check_blank_line_shallow+blank_line_count+1:line_index+blank_line_count]
                self.body.insert(line_index+blank_line_count-(check_blank_line_shallow-1), '')
                blank_line_count -= check_blank_line_shallow - 2
            if check_blank_line_deep != 2:
                del self.body[line_index+blank_line_count+1:line_index+check_blank_line_deep+blank_line_count]
                self.body.insert(line_index+blank_line_count+1, '')
                blank_line_count -= check_blank_line_deep - 2

    def check_link(self, vaild_link: bool = False) -> None:
        '''
        リンクが入った行を整形します。
        1. URLのみの場合→`[hoge](hoge)`の形式に変更します。
        2. 文の中にURLがある場合→`~~~[hoge](hoge)~~~`に変更します。

        Args:
            vaild_link (bool): Markdown内のURLのリンクが存在しているかをチェックする。
        '''
        for index, line in enumerate(self.body):
            link = re.search(r'https?:\/\/[^(\s|\]|\))]+', line)
            if vaild_link and link:
                try:
                    with request.urlopen(link.group()):
                        print(f'[{link.group()}]: OK')
                except error.URLError as err:
                    sys.exit(f'[{link.group()}] is {err.reason}')
            if re.match(r'.*\[.+\]\(.+\).*', line) is None:
                if link:
                    self.body[index] = re.sub(r'(?P<link>https?:\/\/[^\s]+)', r'[\g<link>](\g<link>)', line)

    def check_image(self) -> None:
        '''
        画像タグを整形します。
        1. `<img src='~~' alt='~~~'>`を`![~~](~~~)`に整形します。
        '''
        for index, line in enumerate(self.body):
            is_tag = re.fullmatch(r'^\<img.+\>', line)
            if is_tag:
                img_tag = BeautifulSoup(line, features='html.parser').select('img')[0]
                img_src = img_tag['src']
                try:
                    img_alt = img_tag['alt']
                except KeyError:
                    img_alt = img_src
                self.body[index] = f'![{img_alt}]({img_src})'

    def export_md(self, file_nema: str) -> None:
        '''
        Markdownを新しく保存します。

        Args:
            file_nema (str): 新しく保存するファイル名。
        '''
        save_path = os.path.join(self.save_file_dir, file_nema+'.md')
        with open(save_path, mode='w') as save_md_file:
            save_md_file.write('\n'.join(self.body))
