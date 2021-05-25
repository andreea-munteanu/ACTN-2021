import random

from generating_primitive_root import get_prime_divisors, generate_alpha3
from shanks import shanks, modular_exponentiation
from silver_pohlig_hellman import silver_pohlig_hellman


if __name__ == '__main__':
    q = 5
    p = 2 * q + 1  # 11
    alpha = generate_alpha3(p)
    beta = random.randint(1, p-1)
    print(f'alpha = {alpha}')
    print(f'beta = {beta}')

    print("__________________ SHANKS _____________________")
    print(f'discrete logarithm = {shanks(p, beta, alpha)}')
    print(f'alpha ^ log(beta, alpha) % p = {modular_exponentiation(alpha, shanks(p, beta, alpha), p)}')

    print("____________SILVER-POHLIG-HELLMAN______________")
    # the example from the pdf:
    p = 251
    factorization = get_prime_divisors(p - 1)
    print(f'p - 1 = {p - 1} = {factorization}')
    print(silver_pohlig_hellman(factorization, p, 71, 250))  # should be 197




