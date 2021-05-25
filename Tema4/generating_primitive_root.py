import random
import sympy
from sympy import sieve

"""
________________________________________________________________________________________________________________________
1. (2p) Generate α, a primitive root modulo a prime p, where p is an odd prime, using one of the algorithms discussed in 
class (assume that the prime factorization of p-1 is known in advance - the simplest choice will be p = 2q +1, 
where p and q are odd primes). 
________________________________________________________________________________________________________________________
"""


def get_prime_divisors(p):  # works; checked
    """
    Method for obtaining the prime divisors of a number p.

    :param p:
    :return: p = (p1 ** e1) * (p2 **e2) * ...
    """
    divs = []
    for prime_div in sieve.primerange(2, p):
        if p % prime_div == 0:
            copy = p
            power = 0
            while copy % prime_div == 0:
                power += 1
                copy /= prime_div
            pair = (prime_div, power)
            divs.append(pair)
    return divs


# print(get_prime_divisors(100))


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
            if pow(alpha, (p - 1) // r[0], p) == 1:
                ok = 0
        if ok == 1:
            running = False
    return alpha


# for _ in range(10):
#     print(generate_alpha(11), end=' ')  # should only be 2, 6, 7, 8


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


p = 11
# print(f'(method 1) primitive root of modulo p = {p}: ', generate_alpha2(p))


def jacobi(a, n):
    """
    Method for computing the Jacobi symbol (a/n).
    Computation rules:
    (a) (a/n) = (b/n) if a = b mod n.
    (b) (1/n) = 1 and (0/n) = 0.
    (c) (2m/n) = (m/n) if n = ±1 mod 8. Otherwise (2m/n) = ¯(m/n).
    (d) If m and n are both odd, then (m/n) = (n/m) unless both m and n are congruent to 3 mod 4
    in which case (m/n) = ¯(n/m). --> (Quadratic reciprocity)
    :param a:
    :param n:
    :return: (a/n)
    """
    assert (n % 2 == 1), "Invalid input: n must be odd."
    if a == 1:
        return a
    # ensuring that a < n:
    if a > n:
        a = a % n
    t = 1
    while a != 0:
        # rule (c)
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t *= -1
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t *= -1
        a %= n
    return t if n == 1 else 0


def generate_alpha3(p):
    """
    Generating α = a primitive root modulo a prime p.
    (Assume that the prime factorization of p-1 is known in advance - the simplest choice will be p = 2q +1,
    where p and q are odd primes)

    Algorithm is: PrimitiveRootSafePrime(p)

    :param p: odd prime
    :return: α
    """

    alfa = random.randint(2, p-2)  # [2, p-2]
    if jacobi(alfa, p) == -1:
        return alfa
    return p - alfa


# print(f'(method 2) primitive root of modulo p = {p}: ', generate_alpha3(p))
