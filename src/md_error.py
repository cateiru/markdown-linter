# pylint: disable=W0107
class TitleNotFound(Exception):
    '''
    Markdownのタイトル、
    1行目に`#`がついた文がない場合に発生させる。
    '''
    pass
