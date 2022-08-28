from typing import Callable, TypeVar, Sequence

A = TypeVar('A')
B = TypeVar('B')
FA = TypeVar('FA')
FB = TypeVar('FB')

def type_constructor(a):
    return a

def fmap(f: Callable[[A], B], fa: type_constructor(A)) -> FB:
    return f
