def fact(x):
    match x:
        case 0:
            return 1
        case _:
            return x * fact(x - 1)


fact = (lambda x: 1 if x == 0 else fact(x - 1) * x)


def f(g):
    print("in f")
    g(lambda x: None)
