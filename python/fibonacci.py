# -*- coding: utf-8 -*-


def fib(n):
    a, b = 1, 1
    while n:
        a, b = b, a + b
        yield a
        n -= 1

if __name__ == '__main__':
    # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([i for i in fib(10)])
