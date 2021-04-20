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


def modular_reduction(number, mersenne, s):
    """
    Method for implementing the modular reduction of 'number' to the Mersenne number 2 ** s = 'mersenne'.

    :param number:
    :param mersenne: 2 ** n - 1
    :param s: mersenne parameter
    :return:
    """
    # get binary representation of 'number':
    no_bin = format(number, "b")
    s0, s1 = str(), str()
    if len(no_bin) > s:
        for _ in range(0, s):
            s0 = no_bin[len(no_bin)-1] + s0
            no_bin = no_bin[:-1]
        s0, s1 = int(s0, 2), int(no_bin, 2)
    else:
        s0 = int(no_bin, 2)
        s1 = 0
    return s0 + s1 if s0 + s1 < mersenne else s0 + s1 - mersenne


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

