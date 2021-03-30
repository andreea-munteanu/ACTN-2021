import time
import sympy
from sympy.ntheory.modular import crt
from multiprime_RSA import p, q
from multiprime_RSA import modular_inverse, modular_exponentiation
from multiprime_RSA import library_modular_inverse, library_modular_exponentiation, library_check_prime


def get_n(p, q):
    """
    n = p * p * q

    :param p:
    :param q:
    :return: n
    """
    if p != q and library_check_prime(p) and library_check_prime(q):
        return p * p * q
    raise Exception("p, q not valid.")


def phi(p, q):
    """
    phi(n) = p * (p-1) * (q - 1), where n = p * p * q

    :param p:
    :param q:
    :return:
    """
    return (p - 1) * p * (q - 1)


def our_CRT(e, d, p, q, y):
    """
    Chinese Remainder Theorem as performed with our modular exponentiation and inverse.

    :param e:
    :param d:
    :param p:
    :param q:
    :param y:
    :return: result + time
    """
    # time:
    start = time.time()

    x_q = modular_exponentiation(y % q, d % (q - 1), q)

    # Hensel:
    x0 = modular_exponentiation(y % p, d % (p - 1), p)
    x1 = (((y - modular_exponentiation(x0, e, p * p))/p) *
          modular_inverse(e * modular_exponentiation(x0, e - 1, p * p), p)) % p
    x_p2 = int((x1 * p + x0) % (p * p))

    # for CRT:
    # moduli = [p * p, q]
    # residues = [x_p2, x_q]
    # return crt(moduli, residues)[0], time.time() - start

    # CRT:
    N = p * p * q
    N1 = q
    N2 = p * p
    x1 = sympy.mod_inverse(N1, p*p)
    x2 = sympy.mod_inverse(N2, q)
    x = ((x_p2 * x1 * N1) + (x_q * x2 * N2)) % N
    return x, time.time() - start


def library_CRT(e, d, p, q, y):
    """
    Chinese Remainder Theorem as performed with python's preexisting methods
    :param e:
    :param d:
    :param p:
    :param q:
    :param y:
    :return: result + time
    """
    # time:
    start = time.time()

    x_q = library_modular_exponentiation(y % q, d % (q - 1), q)

    # Hensel:
    x0 = library_modular_exponentiation(y % p, d % (p - 1), p)
    x1 = (((y - library_modular_exponentiation(x0, e, p * p)) / p) *
          library_modular_inverse(e * library_modular_exponentiation(x0, e - 1, p * p), p)) % p
    x_p2 = int((x1 * p + x0) % (p * p))

    # for CRT:
    moduli = [p * p, q]
    residues = [x_p2, x_q]
    return crt(moduli, residues)[0], time.time() - start
    # x2 = 0
    # for alfa in range(1, p**2 + 1):
    #     x2 = x1 + alfa * q
    #     if x2 % (p**2) == x_p2:
    #         break
    #
    # return x2 % (p**2 * q), time.time() - start


print("___________MULTI-POWER RSA____________")
print("p =", p)
print("q =", q)
n = get_n(p, q)
print("n =", n)
phi_n = phi(p, q)
print("phi(n) =", phi_n)
e = sympy.randprime(10, 12)
print("e =", e)
d = modular_inverse(e, phi_n)
print("d =", d)
y = 22

computed_crt, t = library_CRT(e, d, p, q, y)
print("library CRT: ", computed_crt, '\n', "time = ", t, sep='')
computed_crt, t = our_CRT(e, d, p, q, y)
print("our CRT: ", computed_crt, '\n', "time = ", t, sep='')