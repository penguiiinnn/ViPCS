def derivative(f, x):
    h = 1.1
    return (f(x + h) - f(x)) / h


def square(x):
    return x * x


def test():
    print(derivative(square, 2))


test()