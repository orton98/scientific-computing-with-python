import bisect2 as b2
import newton2 as n2
import bisection as b1


def f(x):
    return x**2 - x - 1


if __name__ == '__main__':
    epis1 = 0.01
    epis2 = 0.000001

    # #############  PART 1 ############### #
    # bisect 1 find root of equation
    sqrt_two = lambda x: 2.0 - x*x
    eq3 = lambda x: 6 - x - x**3
    seventh_root_126 = lambda x: 126 ** (1/7)
    a = 1
    b = 5

    # root of square root 2
    print("########################################")
    print("Root of Square Root 2 with Epsilon .01 : ")
    x_sqrt_two = b1.bisect1(sqrt_two, a, b, epis1)
    print(x_sqrt_two)
    print(sqrt_two(x_sqrt_two))
    print("\n\n")

    # 7th root 126
    print("########################################")
    print("7th root 126 with Epsilon .01 : ")
    x_seventh_root_126 = b1.bisect1(seventh_root_126, a, b, epis1)
    print(seventh_root_126(x_seventh_root_126))
    print("\n\n")

    # root of p(x) = 6 - x - x^3 with Epsilon .01
    print("########################################")
    print("Root of p(x) = 6 - x - x^3 with Epsilon .01 : ")
    x_eq3 = b1.bisect1(eq3, a, b, epis1)
    print(x_eq3)
    print(eq3(x_eq3))
    print("\n\n")

    # root of p(x) = 6 - x - x^3 with Epsilon .000001
    print("########################################")
    print("Root of p(x) = 6 - x - x^3 with Epsilon .000001 : ")
    x_eq3 = b1.bisect1(eq3, a, b, epis2)
    print(x_eq3)
    print(eq3(x_eq3))
    print("\n\n")

    # #############  PART 2 ############### #

    # bisect 2 find square root of many values(table)
    # for z in (1, 9, 16, 200):
    #     x = b2.sqrt_bisect(z)
    #     print(z, x, x * x)

    # newton2 find square root with newton method
    # n = 327
    # l = 0.00001
    # print(n2.squareRoot(n, l))
