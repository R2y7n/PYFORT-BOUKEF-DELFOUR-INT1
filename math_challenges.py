import math
import random


def factorial(n):
    fct = 1
    for i in range(1, n + 1):
        fct = fct * i
    return fct


def solve_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    x = -b / a

    return a, b, x
