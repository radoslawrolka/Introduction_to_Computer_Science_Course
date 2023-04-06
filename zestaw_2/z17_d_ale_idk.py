import math


def f(x):
    return x ** x


def df(x):
    return (x ** x) * (math.log(x))


def solve():
    x = 1
    eps = 1e-4
    while abs(f(x)) > eps:
        x = x - f(x) / df(x)
    return x


"""
def f(x):
    return x*math.log(x) - math.log(2020)
def df(x):
    return math.log(x) + 1
"""
