import bisect as b1
import bisect2 as b2
import newton2 as n2


def f(x):
    return 6 - x - x**3


if __name__ == '__main__':
    # bisect 1 find root of equation
    x = b1.bisect(f, 2, 0.01)
    print(x, f(x))

    # bisect 2 find square root of many values(table)
    for z in (1, 9, 16, 200):
        x = b2.sqrt_bisect(z)
        print(z, x, x * x)

    # newton2 find square root with newton method
    n = 327
    l = 0.00001
    print(n2.squareRoot(n, l))