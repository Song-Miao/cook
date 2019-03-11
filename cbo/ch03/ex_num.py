# -*- coding:utf-8 -*-


def t01():
    # 浮点数执行指定精度的舍入运算。
    print(round(1.23, 1))  # 1.2
    print(round(1.27, 1))  # 1.1
    # 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，舍入运算会作用在 十位、百位、千位等上面
    print(round(16123, -1))  # 16120
    print(format(1.23456, '0.2f'))


def t02():
    # 对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
    a = 2.1
    b = 4.2
    print(a + b)  # 6.300000000000001

    from decimal import Decimal
    a = Decimal('2.1')
    b = Decimal('4.2')
    print(a + b)

    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))  # 0.0
    import math
    print(math.fsum(nums))


def t03():
    # 数字的格式化输出
    x = 1234.56789
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '^10.1f'))
    print(format(x, 'e'))
    print(format(x, ','))


def t04():
    # 二八十六进制整数
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    x = -1234
    print(format(x, 'b'))

    print(format(2 ** 32 + x, 'b'))


def t05():
    # 字节到大整数的打包与解包
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    a = int.from_bytes(data, 'little')
    print(a)
    b = int.from_bytes(data, 'big')
    print(b)

    print(b.to_bytes(16, 'little'))
    # 小端：低位 存放在 低地址中
    x = 0x01020304
    print(x.to_bytes(4, 'little'))

    # 将一个整数打包为字节字符串，不合适
    x = 234 ** 23
    print(x.to_bytes(x.bit_length(), 'little'))
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, 'little'))


def t06():
    # 创建或测试正无穷、负无穷或; NaN(非数字); 的浮点数
    a = float("inf")
    print(a)
    b = float("-inf")
    print(b)
    c = float('nan')
    print(c)
    d = float('nan')
    print(c == d)


def t07():
    # 分数
    from fractions import Fraction
    a = Fraction(1, 3)
    b = Fraction(3, 4)
    print(a + b)
    c = a * b
    print(c)
    print(c.numerator, c.denominator)


def t08():
    # 随机选择
    import random
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))
    print(random.sample(values, 4))
    print(random.shuffle(values))  #


if __name__ == '__main__':
    t08()
