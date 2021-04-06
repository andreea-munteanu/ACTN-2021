import math
import sympy
from sympy import sieve  # ciurul lui eratostene pentru numere prime


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


def fast_exponentiation(n):
    """
    2 ** n - 1

    :param n:
    :return:
    """
    res = 1
    for i in range(1, n + 1):
        res = res << 1
    res -= 1
    return res


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

    # square root of number:
    sr = int(math.ceil(math.sqrt(no)))

    # trial division of number to check if number has any prime factors in [2, sqrt(no)]
    for div in sieve.primerange(2, sr):
        if no % div == 0:
            print(f'M_{s} = {no} divides by {div}')
            return False

    # building recurring list u, |u| = s - 2
    u = 4
    i = 1
    while i <= s - 2:
        u = (u * u - 2) % no
        # next iteration:
        i += 1

    return bool(u == 0)
