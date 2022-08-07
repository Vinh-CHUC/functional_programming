import functools

def fac(n):
    match n:
       case 1:
            return 1
       case _:
            return n * fac(n-1)
# fac(6)

def fac2(n, acc):
    match n:
        case 1:
            return acc
        case _:
            return fac2(n-1, acc * n)
fac2(5, 1)

def map_sum(l, n, acc):
    match n:
        case -1:
            return  acc
        case _:
            return map_sum(l, n-1, acc + l(n))

def mod(x, y):
    match d := x - y:
        case _ if d < 0:
            return x
        case _:
            return mod(x - y, y)
