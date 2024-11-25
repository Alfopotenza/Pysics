from sys import exception

pi = 3.141592653589793


def rad2deg(rad):
    res = rad / pi * 180
    return round(res, 4)


def deg2rad(deg):
    return deg / 180 * pi


# Calculates the factorial of a number [n!]
def pythagorean_theorem(x: float, y: float) -> float:
    return (x ** 2 + y ** 2) ** 0.5


def factorial(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


def cos(angle, n=100):
    angle = deg2rad(angle)
    value = 0
    for i in range(n):
        value += (((-1) ** i) / factorial(2 * i)) * (angle ** (2 * i))
    return value


def sin(angle, n=100):
    angle = deg2rad(angle)
    value = 0
    for i in range(n):
        value += (((-1) ** i) / factorial(2 * i + 1)) * (angle ** (2 * i + 1))
    return value


def arctan(x, tolerance=1e-10, max_iterations=1000):
    result = 0
    term = x
    n = 0
    while abs(term) > tolerance and n < max_iterations:
        if n % 2 == 0:
            result += term  # Add the even terms
        else:
            result -= term  # Subtract the odd terms
        n += 1
        term *= x * x  # Move to the next power of x
        term /= (2 * n + 1)  # Factorial for the arctan series
    return result


def atan_large(x):
    if x > 1:
        return 3.141592653589793 / 2 - arctan(1 / x)
    elif x < -1:
        return -3.141592653589793 / 2 - arctan(1 / x)
    else:
        return arctan(x)


def atan2(y, x):
    if x == 0:
        if y > 0:
            return pi / 2
        if y < 0:
            return -pi / 2
        else:
            raise exception("can't put 0, 0")
    if y == 0:
        if x > 0:
            return 0
        else:
            return pi
    base_angle = atan_large(y / x)
    if x > 0:
        print(base_angle)
        return base_angle
    elif x < 0:
        if y >= 0:
            return base_angle + pi
        else:
            return base_angle - pi
