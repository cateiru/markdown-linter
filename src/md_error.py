# pylint: disable=W0107
class TitleNotFound(Exception):
    '''
    Markdownのタイトル、
    1行目に`#`がついた文がない場合に発生させる。
    '''
    pass


class FormatError(Exception):
    '''
    不正確な書式・
    例: タイトルの文中に`#`が存在する。
    '''
    pass
