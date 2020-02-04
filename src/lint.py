'''
Markdownの整形をするプログラム。
'''
import os
from glob import glob

import click

from src.analysis import Analysis


@click.command()
@click.option('--file-path', 'file_path', prompt=True, type=click.Path(exists=True),
              help='`.md` file path or directory path.')
def main(file_path: str) -> None:
    '''
    `.md`ファイルを全て静的解析、整形をします。
    1. ディレクトリを指定する場合はその中の`.md`ファイルを全て静的解析、整形をします。
    2. `.md`ファイルを直接指定する場合はそれを静的解析、整形をします。

    Args:
        file_path (str): [description]
    '''

    if os.path.isdir(file_path):
        __lint_dir(file_path)
    else:
        __lint_file(file_path)


def __lint_dir(directory: str) -> None:
    '''
    ディレクトリから`.md`を抽出し、それら全てを静的解析、整形します。

    Args:
        directory (str): `.md`ファイルが存在するディレクトリ。

    Raises:
        FileNotFoundError: `.md` file not found.
    '''
    save_file_dir = click.prompt('save direcry.', default=directory)
    md_set_path = glob(os.path.join(directory, '*.md'))

    for md_file in md_set_path:
        old_file_name = os.path.splitext(os.path.basename(md_file))[0]
        new_file_name = click.prompt(
            f'save file name.(read file: {old_file_name}.md)', default='lint_'+old_file_name)
        analysis = Analysis(save_file_dir, md_file)
        analysis.check_blank_line()
        analysis.check_title()
        analysis.check_header()
        analysis.check_link(vaild_link=True)
        analysis.check_image()
        analysis.export_md(new_file_name)
    else:  # pylint: disable=W0120
        raise FileNotFoundError('`.md`file not found.')


def __lint_file(file_path: str) -> None:
    '''
    ファイルを静的解析、整形します。

    Args:
        file_path (str): 静的解析、整形する`.md`ファイル。

    Raises:
        FileNotFounfError: It does not have the extension `.md`.
    '''
    if os.path.splitext(os.path.basename(file_path))[1] != '.md':
        raise FileNotFoundError('It does not have the extension `.md`.')

    directory = os.path.dirname(file_path)
    save_file_dir = click.prompt('save direcry.', default=directory)
    old_file_name = os.path.splitext(os.path.basename(file_path))[0]
    new_file_name = click.prompt(f'save file name.(read file: {old_file_name}.md)', default='lint_'+old_file_name)
    analysis = Analysis(save_file_dir, file_path)
    analysis.check_blank_line()
    analysis.check_title()
    analysis.check_header()
    analysis.check_link(vaild_link=True)
    analysis.check_image()
    analysis.export_md(new_file_name)
