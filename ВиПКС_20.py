def f(x):
    return x * x - 4


def bisection(a, b):
    mid = (a + b) / 2

    if abs(f(mid)) < 0.0001:
        return mid

    if f(a) * f(mid) < 0:
        return bisection(a, mid)
    else:
        return bisection(mid, b)


def test():
    print(bisection(0, 5))


test()