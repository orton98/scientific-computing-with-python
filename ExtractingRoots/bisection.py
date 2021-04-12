def bisect1(f, a, b, epsilon=.000001, maxit=100):
    fa = f(a)
    if abs(fa) < epsilon:
        return a
    fb = f(b)
    if abs(fb) < epsilon:
        return b
    if fa*fb > 0:
        print("f(a) * f(b) not have different sign")
        return None
    iterations = 0
    for i in range(maxit):
        iterations = i
        c = (a + b)/2
        fc = f(c)
        if abs(b-a) < epsilon:
            break
        if abs(fc) < epsilon:
            break
        if fa*fc > 0:
            a, fc = c, fc
        if fb*fc > 0:
            b, fb = c, fc
    print("Function Evaluation(Iterations) = ", iterations)
    return c

