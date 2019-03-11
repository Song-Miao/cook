# -*- coding:utf-8 -*-


# 接受任意数量参数
def avg(first, *rest):
    return first + sum(rest)


def anyargs(x, *args, **kwargs):
    print(x)
    print(args)  # tupple
    print(kwargs)  # dict
    # 1
    # (2, 3, 4)
    # {'a': 1, 'b': 2}


def add(x: int, y: int) -> int:
    return x + y


def foo():
    return 1, 2, 3


def spam(a, b=42):
    print(a, b)


def lam():
    x = 10
    a = lambda y: x + y
    c = lambda y, x=x: x + y
    print(a(10))
    print(c(10))
    x = 20
    b = lambda y: x + y
    print(b(10))

    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(10))


def samp():
    count = 0

    def get():
        return count

    def set(value):
        nonlocal count
        count = value

    def func():
        print('n = ', count)

    func.get_n = get
    func.set_n = set
    return func


if __name__ == '__main__':
    f = samp()
    f.set_n(100)
    print(f.get_n())
