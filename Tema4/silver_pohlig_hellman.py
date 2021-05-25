from shanks import modular_inverse, modular_exponentiation
from generating_primitive_root import get_prime_divisors

"""
________________________________________________________________________________________________________________________
3. (4p) Implement the Silver-Pohlig-Hellman algorithm for computing discrete logarithms modulo a large prime p 
(e.g., p is on 1024 bits). Assume that p - 1 has only small prime divisors and that its prime factorization 
is known in advance.
________________________________________________________________________________________________________________________ 

"""


# def silver_pohlig_hellman(alpha, n, beta):
#     """
#
#     :param alpha: generator of cyclic group G
#     :param n: order of cyclic group G
#     :param beta: element belonging to G
#     :return: discrete logarithm x = log_alpha(beta)
#     """
#     prime_divs = get_prime_divisors(n)
#     r = len(prime_divs)
#     for pair in prime_divs:
#         q = pair[0]
#         e = pair[1]
#         lambdaa = 1
#         l = 0  # l(-1)
#         x_i = l
#         power = 1
#         alpha_bar = pow(alpha, n/q)
#
#         for j in range(e-1):
#             lambdaa *= pow(alpha, l * (q ** (j - 1)) )
#             beta_bar = pow(beta * pow(lambdaa, -1), n / (q ** (j + 1)))
#
#             # aici ar trebui 3.56 (baby-step giant fml):
#             l = math.log(beta_bar, alpha_bar)  # log(x, base)
#             x_i += l * pow(q, power)
#             power += 1
#
#     # computing x, 0 <= x <= n-1, s.t. x = x_i % pow(p_i, e_i) for i = 1,...,r
#     x = 0
#     for i in range(r):
#         # computing x using some Gauss algorithm I can't find
#         pass
#     return x


def compute_x_i(base, power, p, alpha, beta):
    """
    Method for computing x_i in the Pohlig-Hellman algorithm.

    :param base:
    :param power:
    :param p: odd prime
    :param alpha: cyclic group generator
    :param beta: primitive root modulo p, B belongs to G

    :return: x_i = l_0 + l_1 * q + l_2 * (q ** 2) + ...
    """
    beta_copy = beta
    x_i = 0
    alpha_i = dict()
    alpha_i[1] = 0
    alpha_inv = modular_inverse(alpha, p)

    for i in range(1, base):
        alpha_i[modular_exponentiation(alpha, int(i * (p - 1) / base), p)] = i

    for i in range(1, power + 1):
        beta_i = modular_exponentiation(beta_copy, int((p - 1) / (pow(base, i))), p)
        c = alpha_i[beta_i]
        x_i = x_i + c * (base ** (i - 1))
        beta_copy = (beta_copy * modular_exponentiation(alpha_inv, c * pow(base, i - 1), p)) % p
    return x_i


def CRT(factorization, x_i, p):
    """
    Method for implementing the Chinese Remainder Theorem.
    
    :param factorization: prime factorization of p: p = (p1 ** e1) * (p2 ** e2)...
    :param x_i: 
    :param p: odd prime
    :return: 
    """
    x = 0

    for i in range(0, len(factorization)):
        M_i = (p - 1) // pow(factorization[i][0], factorization[i][1])
        y_i = modular_inverse(M_i, pow(factorization[i][0], factorization[i][1]))
        x = (x + (x_i[i] * M_i * y_i) % (p - 1)) % (p - 1)

    return x


def silver_pohlig_hellman(factorization, p, alpha, beta):
    """
    Method for implementing the Silver-Pohlig-Hellman algorithm for computing x = log(beta, alpha) discrete logarithm.

    :param factorization: prime factorization of p
    :param p: odd prime
    :param alpha: cyclic group generator
    :param beta: primitive root modulo p, B belongs to G
    :return: x = log(beta, alpha)  # logarithm of beta in base alpha
    """
    x_i = []
    for i in range(0, len(factorization)):
        x_i.append(compute_x_i(factorization[i][0], factorization[i][1], p, alpha, beta))
    return CRT(factorization, x_i, p - 1)  # x


p = 11
factorization = get_prime_divisors(p)
print(silver_pohlig_hellman(factorization, p, 64, 182))
