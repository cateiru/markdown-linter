'''
Markdownの整形をするプログラム。
'''
import os
from glob import glob
from typing import List

import click

from analysis import Analysis


@click.command()
@click.option('--directory', prompt=True, type=click.Path(exists=True), help='`.md` directory path.')
def main(directory: str) -> None:
    '''
    メイン。
    指定したディレクトリ内の全ての`.md`ファイルを全て静的解析、整形をします。

    Args:
        directory (str): [description]
    '''
    save_file_dir = click.prompt('save direcry.', default=directory)
    md_set_path = __find_md(directory)

    for md_file in md_set_path:
        old_file_name = os.path.splitext(os.path.basename(md_file))[0]
        new_file_name = click.prompt(f'save file name.(read file: {old_file_name}.md)', default='new_'+old_file_name)
        analysis = Analysis(save_file_dir, md_file)
        analysis.check_title()
        analysis.export_md(new_file_name)


def __find_md(directory: str) -> List[str]:
    '''
    指定されたディレクトリから全ての`.md`のファイルをリストとして返します。

    Args:
        directory (str): `.md`が格納されているディレクトリ。

    Returns:
        List[str]: 引数のディレクトリ内に入っていた全ての`.md`ファイルの絶対パス。
    '''
    return glob(os.path.join(directory, '*.md'))


if __name__ == "__main__":
    main()  # pylint: disable=E1120
