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

# Abstracting the inner self application, making the self-application more explicit
mkrec_nice_7_2 = lambda g: (
    (
        lambda rec: g(lambda y: rec(rec)(y))
    )
    (
        lambda rec: g(lambda y: rec(rec)(y))
    )
)
# Y = mkrec_nice_7_2
# Y(g) = (lambda r: g(lambda y: r(r)(y)))(lambda r: g(lambda y: r(r)(y)))
# Y(g) = g(lambda y: (lambda r: g(lambda y: r(r)(y)))(lambda r: g(lambda y: r(r)(y)))(y))
# We can step inside the function g!
# Then when we get to the recursive call it'll repeat itself!
fact7_2 = mkrec_nice_7_2(lambda rec_nice: lambda x: 1 if x == 0 else rec_nice(x - 1) * x)

# The real y-combinator, it will spin out of control given that python eagerly evaluates
mkrec_nice8 = lambda g: (
    (
        lambda rec: g(rec(rec))
    )
    (
        lambda rec: g(rec(rec))
    )
)
# Y = mkrec_nice8
# Y(g) = (lambda r: g(r(r)))(lambda r: g(r(r)))
# Y(g) = g((lambda r: g(r(r)))(lambda r: g(r(r)))) = Y(Y(f))
# g is kind of irrelevant here it chould have 0 arguments, but as the language is lazy this will
# never terminate = by lazy here is that we try to fully evaluate the leaves of the tree 
# No dangling
fact8 = mkrec_nice8(lambda rec_nice: lambda x: 1 if x == 0 else rec_nice(x - 1) * x)
