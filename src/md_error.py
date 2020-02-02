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


class MD001(Exception):
    '''
    Heading levels should only increment by one level at a time
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md001---heading-levels-should-only-increment-by-one-level-at-a-time
    '''
    pass


class MD002(Exception):
    '''
    First heading should be a top level heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md002---first-heading-should-be-a-top-level-heading
    '''
    pass


class MD003(Exception):
    '''
    Heading style
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md003---heading-style
    '''
    pass


class MD004(Exception):
    '''
    Unordered list style
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md004---unordered-list-style
    '''
    pass


class MD005(Exception):
    '''
    Inconsistent indentation for list items at the same level
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md005---inconsistent-indentation-for-list-items-at-the-same-level
    '''
    pass


class MD006(Exception):
    '''
    Consider starting bulleted lists at the beginning of the line
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md006---consider-starting-bulleted-lists-at-the-beginning-of-the-line
    '''
    pass


class MD007(Exception):
    '''
    Unordered list indentation
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md007---unordered-list-indentation
    '''
    pass


class MD009(Exception):
    '''
    Trailing spaces
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md009---trailing-spaces
    '''
    pass


class MD010(Exception):
    '''
    Hard tabs
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md010---hard-tabs
    '''
    pass


class MD011(Exception):
    '''
    Reversed link syntax
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md011---reversed-link-syntax
    '''
    pass


class MD012(Exception):
    '''
     Multiple consecutive blank lines
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md012---multiple-consecutive-blank-lines
    '''
    pass


class MD013(Exception):
    '''
    Line length
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md013---line-length
    '''
    pass


class MD014(Exception):
    '''
    Dollar signs used before commands without showing output
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md014---dollar-signs-used-before-commands-without-showing-output
    '''
    pass


class MD018(Exception):
    '''
    No space after hash on atx style heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md018---no-space-after-hash-on-atx-style-heading
    '''
    pass


class MD019(Exception):
    '''
    Multiple spaces after hash on atx style heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md019---multiple-spaces-after-hash-on-atx-style-heading
    '''
    pass


class MD020(Exception):
    '''
    No space inside hashes on closed atx style heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md020---no-space-inside-hashes-on-closed-atx-style-heading
    '''
    pass


class MD021(Exception):
    '''
    Multiple spaces inside hashes on closed atx style heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md021---multiple-spaces-inside-hashes-on-closed-atx-style-heading
    '''
    pass


class MD022(Exception):
    '''
    Headings should be surrounded by blank lines
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md022---headings-should-be-surrounded-by-blank-lines
    '''
    pass


class MD023(Exception):
    '''
    Headings must start at the beginning of the line
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md023---headings-must-start-at-the-beginning-of-the-line
    '''
    pass


class MD024(Exception):
    '''
    Multiple headings with the same content
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md024---multiple-headings-with-the-same-content
    '''
    pass


class MD025(Exception):
    '''
    Multiple top level headings in the same document
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md025---multiple-top-level-headings-in-the-same-document
    '''
    pass


class MD026(Exception):
    '''
    Trailing punctuation in heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md026---trailing-punctuation-in-heading
    '''
    pass


class MD027(Exception):
    '''
    Multiple spaces after blockquote symbol
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md027---multiple-spaces-after-blockquote-symbol
    '''
    pass


class MD028(Exception):
    '''
    Blank line inside blockquote
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md028---blank-line-inside-blockquote
    '''
    pass


class MD029(Exception):
    '''
    Ordered list item prefix
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md029---ordered-list-item-prefix
    '''
    pass


class MD030(Exception):
    '''
    Spaces after list markers
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md030---spaces-after-list-markers
    '''
    pass


class MD031(Exception):
    '''
    Fenced code blocks should be surrounded by blank lines
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md031---fenced-code-blocks-should-be-surrounded-by-blank-lines
    '''
    pass


class MD032(Exception):
    '''
    Lists should be surrounded by blank lines
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md032---lists-should-be-surrounded-by-blank-lines
    '''
    pass


class MD033(Exception):
    '''
    Inline HTML
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md033---inline-html
    '''
    pass


class MD034(Exception):
    '''
    Bare URL used
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md034---bare-url-used
    '''
    pass


class MD035(Exception):
    '''
    Horizontal rule style
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md035---horizontal-rule-style
    '''
    pass


class MD036(Exception):
    '''
    Emphasis used instead of a heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md036---emphasis-used-instead-of-a-heading
    '''
    pass


class MD037(Exception):
    '''
    Spaces inside emphasis markers
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md037---spaces-inside-emphasis-markers
    '''
    pass


class MD038(Exception):
    '''
    Spaces inside code span elements
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md038---spaces-inside-code-span-elements
    '''
    pass


class MD039(Exception):
    '''
    Spaces inside link text
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md039---spaces-inside-link-text
    '''
    pass


class MD040(Exception):
    '''
    Fenced code blocks should have a language specified
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md040---fenced-code-blocks-should-have-a-language-specified
    '''
    pass


class MD041(Exception):
    '''
    First line in file should be a top level heading
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md041---first-line-in-file-should-be-a-top-level-heading
    '''
    pass


class MD042(Exception):
    '''
    No empty links
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md042---no-empty-links
    '''
    pass


class MD043(Exception):
    '''
    Required heading structure
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md043---required-heading-structure
    '''
    pass


class MD044(Exception):
    '''
    Proper names should have the correct capitalization
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md044---proper-names-should-have-the-correct-capitalization
    '''
    pass


class MD045(Exception):
    '''
    Images should have alternate text (alt text)
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md045---images-should-have-alternate-text-alt-text
    '''
    pass


class MD046(Exception):
    '''
    Code block style
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md046---code-block-style
    '''
    pass


class MD047(Exception):
    '''
    Files should end with a single newline character
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md047---files-should-end-with-a-single-newline-character
    '''
    pass


class MD048(Exception):
    '''
    Code fence style
    https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md#md048---code-fence-style
    '''
    pass
