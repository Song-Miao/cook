# -*- coding:utf-8 -*-


def t01():
    # 需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格); 并不是固定
    line = "jdjeior;jdfklajfd  ;dflasf lsjfkl,fjdlks, alsfls"
    import re
    r = re.split(r'[;,\s]\s*', line)
    print(r)
    # 分组捕获一起初出现
    r = re.split(r'(;|,|\s)\s*', line)
    # ['jdjeior', ';', 'jdfklajfd', ' ', '', ';', 'dflasf', ' ', 'lsjfkl', ',', 'fjdlks', ',', 'alsfls']
    print(r)
    values = r[::2]
    delims = r[1::2]
    print(values, delims)


def t02():
    # 字符串开头或结尾匹配
    s = "spam.txt"
    print(s.startswith("http"))
    print(s.endswith(".txt"))
    # 多个匹配项
    r = s.endswith(('.c', '.py', '.txt'))
    print(r)


def t03():
    # 使用Unix Shell中常用的通配符(比如 *.py, Dat[0 - 9] *.csv; 等) 去匹配文本字符串
    from fnmatch import fnmatch, fnmatchcase
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Date45.txt', 'Date[0-9]*'))
    # fnmatch()函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来 匹配模式
    # 匹配能力介于简单的字符串方法和强大的正则表达式之间。如果在
    # 数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案


def t04():
    # 匹配或者搜索特定模式的文本
    # str.find(), str.endswith(), str.startswith()
    import re
    dat = '2019-01-01'
    if re.match(r'\d+-\d+-\d+', dat):
        print('yes')
    print(re.match(r'\d+-\d+-\d+', 'ssss'))  # None

    # 同一个模式去做多次匹配
    pat = re.compile(r'(\d+)-(\d+)-(\d+)')
    if pat.match('2019-01-01'):
        print('yes')
    else:
        print('no')
    if pat.match('20-19'):
        print('yes')
    else:
        print('no')
    # match()从字符串开始去匹配，
    # 如果查找字符串任意部分的模式出现位置，
    # 使用findall() 方法去代替
    text = 'today is 2019-01-01 after day is 2019-01-02'
    print(pat.findall(text))  # [('2019', '01', '01'), ('2019', '01', '02')]
    for year, mon, day in pat.findall(text):
        print('{}-{}-{}'.format(year, mon, day))


def t05():
    # 字符串搜索和替换
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah', 'yep'))

    # sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    import re
    r = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(r)

    # 更加复杂的替换，可以传递一个替换回调函数来代替
    from calendar import month_abbr

    def change(m):
        mon = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon, m.group(3))

    r = re.sub(r'(\d+)/(\d+)/(\d+)', change, text)
    print(r)


def t06():
    # 最短匹配模式
    import re
    str_pat = re.compile(r'\"(.*)\"')
    text = 'Computer says "no." Phone says "yes."'
    r = str_pat.findall(text)
    print(r)

    str_pat2 = re.compile(r'\"(.*?)\"')
    r = str_pat2.findall(text)
    print(r)


def t07():
    # 多行匹配模式
    # 1. \n
    # 2. dotall
    text = ''' /* lajfdklsafdl
    fjlsjfladlfjls */
    '''
    import re
    pat = re.compile(r'/\*(.*?)\*/')
    print(pat.findall(text))
    pat = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(pat.findall(text))

    pat = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
    print(pat.findall(text))


def t08():
    # strip() 方法能用于删除开始或结尾的字符。
    # lstrip(); 和; rstrip(); 分别从左和; 从右执行删除操作
    pass


def t09():
    # 字符串对齐
    text = "hello world"
    print(text.ljust(20, "*"))
    print(text.rjust(20, "-"))
    print(text.center(20, "-"))
    print(format(text, '*>20'))
    print(format(text, '*<20'))
    print(format(text, '*^20'))


def t10():
    # 合并字符串 join
    print('，'.join(['a', 'b']))
    pass


def t11():
    # 内嵌变量的字符串
    s = '{name} has {n} messages'
    print(s.format(name="GG", n=13))
    print(s.format_map({'name': "GG", 'n': 13}))

    name = "MM"
    n = 21
    print(vars())
    print("formadt map: ", s.format_map(vars()))

    class Info:
        def __init__(self, m, z):
            self.name = m
            self.n = z

    i = Info("XX", 12)
    print("with cls: ", s.format_map(vars(i)))

    class Sub(dict):
        def __missing__(self, key):
            return "{" + key + "}"

    del n
    print("sub:", s.format_map(Sub(vars())))


def t12():
    # 以指定列宽格式化字符串 textwrap
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
     the eyes, not around the eyes, don't look around the eyes, \
      look into my eyes, you're under."
    print(s)
    import textwrap
    print()
    print(textwrap.fill(s, 70))
    print()
    print(textwrap.fill(s, 40))
    print()
    print(textwrap.fill(s, 40, initial_indent="    "))


def t13():
    # 在字符串中处理; html; 和; xml
    s = 'Elements are written as "<tag>text</tag>".'
    import html
    print(s)
    ss = html.escape(s)
    print(ss)
    print(html.unescape(ss))


# def t14():
#     # 一个字符串，想从左至右将其解析为一个令牌流
#     text = 'foo=23+42*10'
#     import re
#     NAME = r'(?P<NAME>[a-zA-Z_]*)'
#     NUM = r'(?P<NUM>\d+)'
#     PLUS = r'(?P<PLUS>\+)'
#     TIMES = r'(?P<TIMES>\*)'
#     EQ = r'(?P<EQ>=*)'
#     WS = r'(?P<WS>\s+)'
#
#     pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
#     from collections import namedtuple
#
#     def gegerate(pa, text):
#         Token = namedtuple('Token', ['type', 'value'])
#         scanner = pa.scanner(text)
#         for m in iter(scanner.match, None):
#             yield Token( m.lastgroup, m.group())
#
#     for tok in gegerate(pat, 'foo = 42'):
#         print(tok)


if __name__ == '__main__':
    t01()
