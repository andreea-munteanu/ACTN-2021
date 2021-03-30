import math
import time
import sympy
from sympy.ntheory.modular import crt


def check_prime(n) -> bool:
    """
    Determines whether a number n is prime.

    :param n: number n
    :return: true if number is prime, false otherwise
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for div in range(3, int(math.ceil(math.sqrt(n)))):
        if n % div == 0:
            return False
    return True


def library_check_prime(n) -> bool:
    """
    Library method for determining whether a number is prime.

    :param n:
    :return: true if n is prime (for numbers > 2^64, result can be pseudo-prime), false otherwise
    """
    # return check_prime(n)
    return sympy.isprime(n)


def get_n(p, q, r):
    """
    Get n by formula: n = pqr, where n,p,q are 512-bit distinct prime numbers.

    :param p:
    :param q:
    :param r:
    :return: n
    """
    if p != q != r and check_prime(p) and check_prime(q) and check_prime(r):
        return p * q * r
    else:
        raise Exception("p, q, r not valid.")


def phi(p, q, r):
    """
    phi(n) = (p-1) * (q-1) * (r-1)

    :param p:
    :param q:
    :param r:
    :return: phi(n)
    """
    return (p-1) * (q-1) * (r-1)


def encryption(x, e, n):
    """
    enc(x) = x^e mod n
    :param x:
    :return:
    """
    return modular_exponentiation(x, e, n)


def library_modular_exponentiation(a, n, m):
    """
    (a ^ n) mod m from python library.

    :param a:
    :param m:
    :return: (a ^ n) mod m
    """
    return pow(a, n, m)


def modular_exponentiation(a, n, m):
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


def library_modular_inverse(a, m):
    """
    Use sympy.mod_inverse(a, m) to return a number c such that, (a * c) = 1 (mod m).

    :param a:
    :param m:
    :return: c
    """
    return sympy.mod_inverse(a, m)


def modular_inverse(a, m):
    """
    :param a:
    :param m:
    :return: a ^ (-1) mod m.
    """

    def egcd(a, b):
        """
        Euclidean GPC algorithm.

        :param a:
        :param b:
        :return: gpc(a, b)
        """
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % m


def our_CRT(y, d, p, q, r):
    """
    Chinese Remainder Theorem as performed with our modular exponentiation and inverse.

    :param y:
    :param d:
    :param p:
    :param q:
    :param r:
    :return: CRT result + computation time
    """
    # time:
    start = time.time()
    # Fermat for computing x_p, x_q, x_r:
    x_p = modular_exponentiation(y % p, d % (p-1), p)
    x_q = modular_exponentiation(y % q, d % (q - 1), q)
    x_r = modular_exponentiation(y % r, d % (r-1), r)

    # CRT the school way:
    N = p * q * r
    N1 = N // p
    N2 = N // q
    N3 = N // r

    x1 = sympy.mod_inverse(N1, p)
    x2 = sympy.mod_inverse(N2, q)
    x3 = sympy.mod_inverse(N3, r)

    x = ((x_p * x1 * N1) + (x_q * x2 * N2) + (x_r * x3 * N3)) % N

    # returning CRT result + time
    return x, time.time() - start


def library_CRT(y, d, p, q, r):
    """
    Chinese Remainder Theorem as performed with python's preexisting methods.

    :param y:
    :param d:
    :param p:
    :param q:
    :param r:
    :return: CRT result + computation time
    """
    start = time.time()
    x_p = library_modular_exponentiation(y % p, d % (p-1), p)
    x_q = library_modular_exponentiation(y % q, d % (q - 1), q)
    x_r = library_modular_exponentiation(y % r, d % (r-1), r)
    # data for computing CRT with library's method:
    residues = [int(x_p), int(x_q), int(x_r)]
    moduli = [p, q, r]
    return crt(moduli, residues)[0], time.time() - start


print("___________MULTI-PRIME RSA____________")
p, q, r = sympy.randprime(100, 10000), sympy.randprime(100, 10000), sympy.randprime(100, 10000)
# p = 3
# q = 5
# r = 7
print("p =", p)
print("q =", q)
print("r =", r)
n = get_n(p, q, r)
print("n =", n)

phi_n = phi(p, q, r)
print("phi(n) =", phi_n)
# e = sympy.randprime(3, 5)
e = 3
print("e =", e)
d = library_modular_inverse(e, phi(p, q, r))
print("d =", d)
x = sympy.prime(30)  # n-th prime number
# print("y = enc(x) =", encryption())
y = modular_exponentiation(x, e, n)
computed_crt, t = library_CRT(e, d, p, q, y)
print("library CRT: ", computed_crt, '\n', "time = ", t, sep='')
computed_crt, t = our_CRT(e, d, p, q, y)
print("our CRT: ", computed_crt, '\n', "time = ", t, sep='')
