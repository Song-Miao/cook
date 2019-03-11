# -*- coding:utf-8 -*-


def t01():
    # 遍历一个可迭代对象中的所有元素，但是却不想使用for 循环
    with open("/etc/passwd") as f:
        try:
            while True:
                line = next(f)
                print(line, end="")
        except StopIteration:
            pass


def t02():
    # 构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直
    # 接在你的这个新容器对象上执行迭代操作
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return "Node({!r})".format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    root.add_child(c1)
    root.add_child(c2)
    for ch in root:
        print(ch)


def t03():
    # 使用生成器创建新的迭代模式
    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(0, 5, 1.3):
        print(n, end=" ")

    print(list(frange(0, 5, 1.3)))


def t04():
    # 构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return "Node({!r})".format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first()

    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    c3 = Node(3)
    c4 = Node(4)
    c1.add_child(c3)
    c2.add_child(c4)
    root.add_child(c1)
    root.add_child(c2)
    for ch in root.depth_first():
        print(ch)


def t05():
    # 定义一个反向迭代器可以使得代码非常的高效，因为它不再需要将数据填充到一个
    # 列表中然后再去反向迭代这个列表
    with open("/etc/passwd") as f:
        for line in reversed(list(f)):
            print(line, end="")

    class CountDown:
        def __init__(self, start):
            self.start = start

        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    for r in reversed(CountDown(10)):
        print(r, end=" ")
    print()
    for r in CountDown(10):
        print(r, end=" ")

    print()
    import itertools
    for x in itertools.islice(CountDown(10), 5, 10):
        print(x)


def t06():
    # 定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值
    from collections import deque

    class linehistory:
        def __init__(self, lines, hislen=3):
            self.lines = lines
            self.history = deque(maxlen=hislen)

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line


def t07():
    # 一个由迭代器生成的切片对象，但是标准切片操作并不能做到 isslice
    t05()


def t08():
    a = [1, 2, 3, 4, 5, 6]
    from itertools import dropwhile
    for i in dropwhile(lambda i: i < 4, iter(a)):
        print(i, end=" ")

    from itertools import permutations
    arr = ['a', 'b', 'c']
    for p in permutations(arr):
        print(p)

    from itertools import combinations
    for p in combinations(arr, 2):
        print(p)

    for idx, val in enumerate(arr):
        print(idx, val)

    headers = ['name', 'age', 'shares', 'price']
    for a, b in zip(arr, headers):
        print(a, " zi ", b)

    print(list(zip(arr, headers, headers)))


def t09():
    # 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不
    # 失可读性的情况下避免写重复的循环。
    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)


def t10():
    import heapq
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8]
    for x in heapq.merge(a, b):
        print(x)


if __name__ == '__main__':
    t10()
