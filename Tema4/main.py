import math
import random
import sympy
from sympy import sieve
import numpy as np


"""
1. Generate α, a primitive root modulo a prime p, where p is an odd prime, using one of the algorithms discussed in 
class (assume that the prime factorization of p-1 is known in advance - the simplest choice will be p = 2q +1, 
where p and q are odd primes). (2p)

2. For p and α generated as above and an arbitrary β, compute logarithm modulo p to the base α of β, using one of 
the algorithms discussed in class (Skanks or Pollard). Use moderate-sized primes (e.g., p is on 32 bits). (4p)

3. Implement the Silver-Pohlig-Hellman algorithm for computing discrete logarithms modulo a large prime p 
(e.g., p is on 1024 bits). Assume that p - 1 has only small prime divisors and that its prime factorization 
is known in advance. (4p)
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


def pollard_rho(alpha, n, beta):
    """

    :param alpha: generator of cyclic group G
    :param n: order of cyclic group G
    :param beta: element belonging to G
    :return: discrete logarithm x = log_alpha(beta)
    """
    x = a = b = np.zeros(n)
    x[0] = 1
    a[0] = b[0] = 0
    for i in range(1, n):
        pass


def pohlig_hellman(alpha, n, beta):
    """

    :param alpha: generator of cyclic group G
    :param n: order of cyclic group G
    :param beta: element belonging to G
    :return: discrete logarithm x = log_alpha(beta)
    """
    prime_divs = get_prime_divisors(n)
    r = len(prime_divs)
    for pair in prime_divs:
        q = pair[0]
        e = pair[1]
        lambdaa = 1
        l = 0  # l(-1)
        x_i = l
        power = 1
        alpha_bar = pow(alpha, n/q)

        for j in range(e-1):
            lambdaa *= pow(alpha, l * (q ** (j - 1)) )
            beta_bar = pow(beta * pow(lambdaa, -1), n / (q ** (j + 1)))

            # aici ar trebui 3.56 (baby-step giant fml):
            l = math.log(beta_bar, alpha_bar)  # log(x, base)
            x_i += l * pow(q, power)
            power += 1

    # computing x, 0 <= x <= n-1, s.t. x = x_i % pow(p_i, e_i) for i = 1,...,r
    x = 0
    for i in range(r):
        # computing x using some Gauss algorithm I can't find
        pass
    return x


if __name__ == '__main__':
    q = 5
    p = 2 * q + 1  # 7, 11
    print(f'primitive root of modulo p = {p}: ', generate_alpha2(p))

