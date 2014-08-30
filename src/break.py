#! /usr/bin/python

# 下面是找到2-10(不包含10)中的素数
# range(2,2)为空列表
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, '=', x, '*', n/x
            break
    else:
        print n, 'is a prime number'


# 注意，else与内部for语句对应，如果与if语句对应会是另一番结局
