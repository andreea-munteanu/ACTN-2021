import math


"""
________________________________________________________________________________________________________________________
2. (4p) For p and α generated as above and an arbitrary β, compute logarithm modulo p to the base α of β,
using one of the algorithms discussed in class (Skanks or Pollard). Use moderate-sized primes (e.g., p is on 32 bits).
________________________________________________________________________________________________________________________

"""


def modular_exponentiation(a, n, m):  # works; checked
    """
    (a ^ n) mod m as computed by ourselves.
    :param a:
    :param n:
    :param m:
    :return: (a ^ n) mod m
    """
    if m == 1:
        return 0

    res = 1
    a = a % m
    while n:
        if n % 2 == 1:
            res = (res * a) % m
        n = n >> 1
        a = (a ** 2) % m
    return res


def baby_steps(alpha, m, p):
    """
    Method for constructing table with entries (j, alpha ** j)

    :param alpha: cyclic group generator
    :param m:
    :param p: odd prime
    :return: table L = (j, alpha ** j)
    """
    L = []
    for j in range(0, m):
        g = modular_exponentiation(alpha, j, p)
        L.append((j, g))
    L = sorted(L, key=lambda x: x[1]).copy()
    return L


def modular_inverse(a, m):
    """
    Method for computing the modular inverse.

    :param a:
    :param m:
    :return: a ** (-1) mod m
    """
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        if m != 0:
            q = a // m
        t = m
        if m != 0:
            m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x


def giant_steps(beta, alpha, m, p):
    """
    Method for implementing baby-step giant-step algorithm: looking for the i indexes.

    :param alpha: cyclic group generator
    :param m:
    :param p: odd prime
    :return: table L = (j, alpha ** j)
    """
    L = []
    for i in range(0, m):
        alpha_inverse = modular_inverse(alpha, p)
        h = (beta * modular_exponentiation(alpha_inverse, m*i, p)) % p
        L.append((i, h))
    return L


def shanks(p, beta, alpha):
    """
    Method for implementing the Shanks algorithm for computing the discrete logarithm.
    We want to find indexes i, j s.t. pow(alpha, x) = pow(alpha, i * m + j). --> baby giant step

    :param p: odd prime number
    :param alpha: generator of cyclic group G
    :param beta: element belonging to G
    :return: discrete logarithm x = log_alpha(beta)
    """
    m = math.floor((p - 1) ** (1/2))

    list_of_js = baby_steps(alpha, m, p)
    list_of_is = giant_steps(beta, alpha, m, p)

    x, i, j = 0, 0, 0

    for i in range(0, len(list_of_is)):
        for j in range(0, len(list_of_js)):
            if list_of_is[i][1] == list_of_js[j][1]:
                i = list_of_is[i][0]
                j = list_of_js[j][0]
                break

    return i * m + j  # x

