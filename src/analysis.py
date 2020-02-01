'''
main
'''
import os
import re
from typing import List

import md_error


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
            return [s.strip() for s in md_file.readlines()]

    def check_title(self) -> str:
        '''
        Markdownのタイトルを整形します。
        1. `#`とタイトル文の間に空白を開けます。
        2. タイトルは一番トップレベルの行であり、その上には何もありません。
        3. タイトルの下の行は1つの空白行があります。

        Raises:
            TitleNotFound: Markdown内にタイトルが存在しない場合。

        Returns:
            str: タイトルの本文
        '''
        for line in self.body:
            title = re.fullmatch(r'\#\s?(?P<title>.+)', line)
            if title:
                title_body = title.group('title')
                title_line = self.body.index(line)
                break
        else:
            raise md_error.TitleNotFound('Title not found.')

        self.body.insert(0, f'# {title_body}')
        del self.body[title_line+1]

        check_blank_line = 1
        while self.body[check_blank_line] == '':
            check_blank_line += 1
        if check_blank_line != 2:
            del self.body[1:check_blank_line]
            self.body.insert(1, '')

        return title_body

    def export_md(self, file_nema: str) -> None:
        '''
        Markdownを新しく保存します。

        Args:
            file_nema (str): 新しく保存するファイル名。
        '''
        save_path = os.path.join(self.save_file_dir, file_nema+'.md')
        with open(save_path, mode='w') as save_md_file:
            save_md_file.write('\n'.join(self.body))
