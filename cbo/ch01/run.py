# -*- coding:utf-8 -*-


# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值 给 N 个变量
def t01():
    p = (4, 5)
    x, y = p
    print(x)
    print(y)

    data = ['acme', 50, 91.1, (2019, 11, 21)]
    name, share, _, (y, _, d) = data
    print(name, share, y, d)

    s = 'hello'
    a, b, c, d, e = s
    print(a, b, c, d, e)


def t02():
    # 解压可迭代对象赋值给多个变量
    data = ['acme', 50, 91.1, (2019, 11, 21)]
    a, *b, c = data
    print(a, b, c)

    records = [('foo', 1, 2),
               ('bar', 'hello', 1),
               ('foo', 3, 4), ]

    def t022(z, y):
        print(z, y)

    for x, *args in records:
        t022(*args)

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *_, sh = line.split(":")
    print(uname, sh)


def t03():
    # yield 生成器
    # 保留最后有限几个元素
    def yieldfoo():
        print("starting...")
        while True:
            res = yield 4
            print("res", res)

    g = yieldfoo()
    print(next(g))
    print("*" * 20)
    print(next(g))

    from collections import deque

    def search():
        lines = deque(maxlen=4)
        for i in range(10):
            yield i, lines
            lines.append(i)

    m = search()
    for i, lines in search():
        for pline in lines:
            print(pline, end=" ")
        print("=> end !!! i ", i, end=" ")
        print("-" * 20)


def t04():
    # 获得最大或者最小的; N; 个元素列表
    import heapq
    nums = [1, 100, 3, 44, 6, 33]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portinfo = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, portinfo, key=lambda s: s['price']))


def t05():
    import heapq
    # 利用; heapq; 模块实现了一个简单的优先级队列

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

    q = PriorityQueue()
    q.push("abc", 1)
    q.push("ddd", 3)
    q.push("dee", 2)
    print(q.pop())
    print(q.pop())
    print(q.pop())


def t06():
    # 创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
    from collections import OrderedDict
    # d = dict()  # ??
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 1
    d['span'] = 1
    d['grok'] = 4
    d['aut'] = 1
    for key in d:
        print(key, d[key])
    import json
    print(json.dumps(d))


def t07():
    # 数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)
    prices = {'ACME': 45.23,
              'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
              }
    print(max(zip(prices.values(), prices.keys())))
    print(sorted(zip(prices.values(), prices.keys())))


def t08():
    # 在两个字典中寻寻找相同点(比如相同的键、相同的值等等)
    # 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返 回结果上执行集合操作
    a = {
        'x': 1,
        'y': 2,
        'z': 3}
    b = {
        'w': 10,
        'x': 11,
        'y': 2}
    print(a.keys() & b.keys())


def t09():
    # 在一个序列上面保持元素顺序的同时消除重复的值
    def dedupe(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    r = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
    print(r)


def t10():
    # 命名切片
    a = "sfkjklsdjfjaklfjlksjfeiruweoroiwuroieu"
    s = slice(5, 10, 2)
    print(a[s])


def t11():
    # 找出一个序列中出现次数最多的元素
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
        'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    print(word_counts)
    print(word_counts.most_common(3))

    counts = Counter(words)
    print(word_counts - counts)


def t12():
    # 通过某个关键字排序一个字典列表
    # itemgetter() 有时候也可以用 lambda 表达式代替
    # 但是，使用 itemgetter() 方式会运行的稍微快点
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname1 = sorted(rows, key=lambda x: x['fname'])
    print(rows_by_fname1)
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter("fname"))
    print(rows_by_fname)
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_uid)

    class User:
        def __init__(self, uid):
            self.uid = uid

        def __repr__(self):
            return 'User({})'.format(self.uid)

    users = [User(1), User(32), User(4)]
    print(sorted(users, key=lambda x: x.uid))
    from operator import attrgetter
    print(sorted(users, key=attrgetter('uid')))


def t13():
    # 一个字典或者实例的序列，然后你想根据某个特定的字段比如; date; 来分组迭; 代访问
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]
    from collections import defaultdict
    # defaultdict(); 在dict(); 的基础上添加了一个missing(key); 的方法，
    # 在调用一个不存在的key的时候，defaultdict函数会调用“missing”，
    # 返回一个int, set, list, dict对应的默认数值，不会出现keyerror的情况。
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)
    for key, items in rows_by_date.items():
        print(key, items)


def t14():
    # 一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
    arr = [1, 4, -90, -29, -3, 34, 44]
    f1 = [n for n in arr if n > 0]
    print(f1)

    def foo(val):
        return val < 0

    f2 = list(filter(lambda x: x > 0, arr))
    print(f2)


def t15():
    # 构造一个字典，它是另外一个字典的子集
    prices = {'ACME': 45.23,
              'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
              }
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
    p2 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p2)


def t16():
    # 有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代
    # 码难以阅读，于是你想通过名称来访问元素
    from collections import namedtuple
    Subscr = namedtuple("Subscr", ['addr', 'joined'])
    sub = Subscr("com.abc@qq.com", "20150101")
    print(sub.addr)
    sub = sub._replace(addr='addr')
    print(sub.addr)


def t17():
    # 有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些;
    # 操作，比如查找值或者检查某些键是否存在
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    from collections import ChainMap
    c = ChainMap(a, b)
    # ChainMap 接受多个字典并将它们在逻辑上变为一个字典。
    # 然后，这些字典并不是真的合并在一起了，
    # ChainMap 类只是在内部创建了一个容纳这些字典的列表并重;
    # 新定义了一些常见的字典操作来遍历这个列表
    print(c['x'])
    print(c['y'])
    print(c['z'])
    values = c.new_child()
    values['x'] = 2
    print(values)
    values = values.new_child()
    values['x'] = 3
    print(values)
    # ChainMap({'x': 2}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})
    # ChainMap({'x': 3}, {'x': 2}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})


if __name__ == '__main__':
    t17()
