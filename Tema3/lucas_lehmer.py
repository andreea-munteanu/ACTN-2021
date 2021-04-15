import math
import sympy
from sympy import sieve


def check_prime(n) -> bool:
    """
    Implementation of primality check for small numbers.

    :param n: number n
    :return: true if n is prime, false otherwise
    """
    # if n < 2:
    #     return False
    # if n in (2, 3):
    #     return True
    # if n % 2 == 0:
    #     return False
    # for div in range(3, int(math.ceil(math.sqrt(n)))):
    #     if n % div == 0:
    #         return False
    # return True
    return sympy.isprime(n)


def fast_exponentiation(p):
    """
    :param p:
    :return: 2 ** p - 1
    """
    return (1 << p) - 1
    # res = 1
    # for i in range(1, p + 1):
    #     res = res << 1
    # res -= 1
    # return res

    # """
    # Calculates b^p
    # Complexity O(log p)
    # """
    # res = 1
    # b = 2
    # while p:
    #     if p & 0x1: res *= b
    #     b *= b
    #     p >>= 1
    #
    # return res - 1
    #
    # return (2 ** p) - 1


def modular_reduction(s, Mn, n):
    """
    Method for implementing the modular reduction of Mersenne number 2 ** s.

    :param s: number
    :param Mn: 2 ** n - 1
    :param n:
    :return:
    """
    s_bin = format(s, "b")
    s0, s1 = str(), str()

    if len(s_bin) <= n:
        s0 = int(s_bin, 2)
        s1 = 0
    else:
        for _ in range(0, n):
            s0 = s_bin[len(s_bin)-1] + s0
            s_bin = s_bin[:-1]
        s1 = s_bin
        s0 = int(s0, 2)
        s1 = int(s1, 2)

    return s0 + s1 if s0 + s1 < Mn else s0 + s1 - Mn


def mersenne_s(s):
    """
    Method for getting the value of Mersenne number 2 ** s - 1, with s ≥ 3.

    :param s: prime number s
    :return: 2 ** s - 1
    """
    # s must be a prime number:
    if not check_prime(s):
        raise ValueError(f's = {s} is not prime.')
    return fast_exponentiation(s)


def lucas_lehmer(s) -> bool:
    """
    Lucas-Lehmer primality test.

    :param s: s
    :return: true if 'no' is prime, false otherwise
    """
    # Mersenne number:
    no = mersenne_s(s)

    # square root of s:
    sr = int(math.ceil(math.sqrt(s)))

    # trial division of number to check if s has any prime factors in [2, sqrt(s)]
    # already covered by the check performed in the function mersenne_s(), but for stringency reasons:
    for div in sieve.primerange(2, sr):
        if s % div == 0:
            print(f'M_{s} = {no} has s divide by {div}. S is not a prime')
            return False

    # building recurring list u, |u| = s - 2
    u = 4
    i = s - 2
    while i:
        u = modular_reduction(u ** 2 - 2, no, s)
        # next iteration:
        i -= 1

    return bool(u == 0)

