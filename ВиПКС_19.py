def factors(n, d=2):
    if n == 1:
        return

    if n % d == 0:
        print(d, end=" ")
        factors(n // d, d)
    else:
        factors(n, d + 1)


def test():
    factors(20)


test()