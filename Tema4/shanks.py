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
    Method for constructing table with entries (j, alpha_j)

    :param alpha: cyclic group generator
    :param m:
    :param p: odd prime
    :return:
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
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x


def giant_steps(beta, alpha, m, p):
    L = []
    for i in range(0, m):
        alpha_to_minus_1 = modular_inverse(alpha, p)
        h = (beta * modular_exponentiation(alpha_to_minus_1, m*i, p)) % p
        L.append((i, h))
    return L


def shanks(p, beta, alpha):
    """
    :param p: odd prime number
    :param alpha: generator of cyclic group G
    :param beta: element belonging to G
    :return: discrete logarithm x = log_alpha(beta)
    """
    m = math.floor((p - 1) ** (1/2))

    L_bs = baby_steps(alpha, m, p)
    L_gs = giant_steps(beta, alpha, m, p)

    x, i, j = 0, 0, 0

    for i in range(0, len(L_gs)):
        for j in range(0, len(L_bs)):
            if L_gs[i][1] == L_bs[j][1]:
                i = L_gs[i][0]
                j = L_bs[j][0]
                break

    return i * m + j  # x

