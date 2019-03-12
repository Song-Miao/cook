# -*- coding:utf-8 -*-


# 改变对象实例的打印或显示输出，让它们更具可读性
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# 通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


# 对象支持上下文管理协议 (with 语句)。
class WithCls:
    def __init__(self):
        pass

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


# 对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 slots 属 性来极大的减少实例所占的内存
# python 就会为实例使用一种更加紧凑的内部表示
class Date2:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# Python 封装数据，通过遵循一定的属性和方法命名规约来达到这个效果。
# 第一个约定是任何以单下划线 开头的名字都应该是内部实现
# 使用双下划线开始会导致访问名称变成其他形式,继承是无法被覆盖
class A:
    def __init__(self):
        self.public = 0
        self._internal = 1
        self.__private = 2


# 给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查 或合法性验证。
class person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('get')
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, int):
            raise TypeError()
        self._name = value


# 创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功能
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise Exception()
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


import math


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


# 公用的 init()函数
class Structure:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise Exception()
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares']


# 抽象类


if __name__ == '__main__':
    print(Pair(1, 2))
    print(str(Pair(1, 2)))

    d = Date(2019, 1, 2)
    print(format(d, 'ymd'))

    with WithCls() as f:
        pass

    p = person(1)
    p.name = 2
    # p.name = '2'

    p = Point(2, 3)
    # p.x = '2'
    print(p.x)

    s = Stock('1', '2')

    # 可以通过 new()方法创建一个未初始化的实例
    print("====")
    print(d.year, d.month, d.day)
    dd = Date.__new__(Date)
    # print(dd.year)
    attr = {'year': 2019, 'month': 1, 'day': 12}
    for k, v in attr.items():
        setattr(dd, k, v)
    print(dd.year, dd.month, dd.day)

    # 通过字符串调用对象方法
    print("===")
    dis = getattr(p, 'distance')(0, 0)
    print(dis)
