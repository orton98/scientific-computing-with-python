from __future__ import print_function, division


def sqrt_bisect(z, tol=1E-12):
    ''' Find the square root of `z` by bisection, with tolerance `tol` '''
    lo, hi = 0, z
    while True:
        mid = (lo + hi) / 2.0
        delta = mid * mid - z
        if abs(delta) < tol:
            break

        if delta > 0:
            # Too high
            hi = mid
        else:
            # Too low
            lo = mid
    return mid
