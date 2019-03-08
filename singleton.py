# -*- coding:utf-8 -*-

print("hello world")

"""
super()方法：
    返回一个父类或兄弟类类型的代理对象，让你能够调用一些从继承过来的方法。
    它有两个典型作用：
        a. 在单继承的类层次结构中，super()可用于引用父类而不显式父类名称，从而使代码更易于维护。
        b. 在多重继承中，可以保证公共父类仅被执行一次。
__new__方法：
    a.它是一个类级别的静态方法。通常用于控制生成一个新实例的过程。
    b.返回的是一个实例化出来的实例
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    pass


a = A()
b = A()
print(a, b)


#####################

# 创建实例时把所有实例的__dict__指向同一个字典,这样它们都具有相同的属性和方法(类的__dict__存储对象属性)
class Singleton2(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class B(Singleton2):
    pass


######################
# def singleton(cls):
#     instance = {}
#
#     def wapper():
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#             return instance[cls]
#
#     return wapper()
class Singleton3(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton3
class C:
    pass


a = C()
b = C()
print(a, b)

######################
#  作为Python模块时是天然的单例模式
from singleton_import import mysington
