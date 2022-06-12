def fact(x):
    match x:
        case 0:
            return 1
        case _:
            return x * fact(x - 1)


fact2 = (lambda x: 1 if x == 0 else fact(x - 1) * x)


# F will call itself twice
def f(g):
    print("in f")
    g(lambda x: None)


# F is properly recursive
def f2(g):
    print("in f")
    return lambda: g(g)


def fact_base3(rec, x):
    match x:
        case 0:
            return 1
        case _:
            return x * rec(rec, x - 1)


def fact3(x):
    return fact_base3(fact_base3, x)


fact_base4 = lambda rec, x: 1 if x == 0 else x * rec(rec, x - 1)
fact4 = (lambda x: fact_base4(fact_base4, x))

# With currying
fact_base5 = lambda rec: (lambda x: 1 if x == 0 else x * rec(rec)(x - 1))
fact5 = fact_base5(fact_base5)

# Abstracting the outer self application
mkrec = lambda f: f(f)
fact6 = mkrec(lambda rec: lambda x: 1 if x == 0 else rec(rec)(x - 1) * x)

# Abstracting the inner self application
mkrec_nice = lambda g: (
    mkrec(
        lambda rec: g(lambda y: rec(rec)(y))
    )
)
fact7 = mkrec_nice(lambda rec_nice: lambda x: 1 if x == 0 else rec_nice(x - 1) * x)
