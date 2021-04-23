import math
import random
import sympy
from sympy import sieve


def get_prime_divisors(p):
    """
    Method for obtaining the prime divisors of a number p.

    :param p:
    :return:
    """
    divs = []
    for prime_div in sieve.primerange(2, p):
        if (p - 1) % prime_div == 0:
            divs.append(prime_div)
    return divs


def generate_alpha(p):
    """
    Generating α = a primitive root modulo a prime p.
    (Assume that the prime factorization of p-1 is known in advance - the simplest choice will be p = 2q +1,
    where p and q are odd primes)

    :param p: odd prime
    :return: α
    """
    assert sympy.isprime(p), "p should be a prime number"

    # prime factorization of p - 1:
    factorization = get_prime_divisors(p-1)
    print(f'prime factors of {p}: ', factorization)

    # randomly generating alpha s.t. alpha ∈ Z*(p):
    alpha = random.randrange(0, p)
    running = True
    while running:
        alpha = random.randrange(0, p)
        ok = 1
        for r in factorization:
            if pow(alpha, (p - 1)//r, p) == 1:
                ok = 0
        if ok == 1:
            running = False
    return alpha


def generate_alpha2(p):  # works; checked
    """
    Generating α = a primitive root modulo a prime p.
    (Assume that the prime factorization of p-1 is known in advance - the simplest choice will be p = 2q +1,
    where p and q are odd primes)

    :param p: odd prime
    :return: α
    """
    lambda_symbol = random.randint(2, p - 1)
    alpha = (-1) * (lambda_symbol ** 2) % p
    return alpha


if __name__ == '__main__':
    q = 5
    p = 2 * q + 1  # 7, 11
    print(f'primitive root of modulo p = {p}: ', generate_alpha2(p))

