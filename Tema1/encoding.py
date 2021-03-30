"""
Represent the input m as a vector with (k − 1) components over Zp, where p is prime:
m = (ak−1,...,a1);

• Choose the polynomial P(x) = ak−1xk−1 +···+a1x (remark that P(0) = 0 - this property will be used for decoding);
• Encode m as the vector y = (P(1), P(2),...,P(n)), where n = k + 2s,   y = (y1,...,yn).
"""

print("---------- Input data ----------")
m: str = "29"
initial_m = int(m)
print('m =', m)
p = 11  # input()
print('p =', p)
k = len(m) + 1
print('k =', k)
s = 1
print('s =', s)
n = k + 2 * s
print('n =', n)


def modulo_p(a, p):
    """
    :param a: number a
    :param p: prime number p (Zp)
    :return: a % p
    """
    return a % p


def convert_to_base_p(m, p):
    """
    Function for computing the base p equivalent of a number m.

    :param m: number m
    :param p: base
    :return: a string representing the number m in base_p
    """
    res = ""
    while m:
        digit = int(m % p)
        res += str(digit) if digit < 10 else chr(ord('A') + digit - 10)
        m = m // p
    # reversing string
    res = res[::-1]
    return res


print("----- m as vector in Z(p) ------")
m = convert_to_base_p(int(initial_m), p)  # type str
print("m =", initial_m, "in base", p, "is", m)


def m_as_vector(m):
    """
    Method for converting m ∈ Z(p) into a vector of coefficients for polynomial P(X).

    :param m: input m as string
    :return: m represented as vector with k-1 elements
    """
    res = []
    for c in m:
        res.append(int(c))
    # returned reversed vector:
    return res[::-1]


m = m_as_vector(m)
print("P(X) =", m)


def compute_polynomial_horner(coef, point):
    """
    Function for computing the value of a polynomial in a given point using Horner.

    :param coef: vector of coefficients (ex: coef = (a2=2, a1=7))
    :param point: value of polynomial in point value: P(point) = ...
    :return: computed polynomial (in Zp)
    """
    res = coef[-1]
    for i in range(0, len(coef) - 1):
        res = res * point + coef[i]
    return modulo_p(res, p)


def compute_polynomial(coef, point):
    """
    Function for computing the value of a polynomial in a given point using Horner.

    :param coef: vector of coefficients (ex: coef = (a2=2, a1=7))
    :param point: value of polynomial in point value: P(point) = ...
    :return: computed polynomial (in Zp)
    """
    res = 0
    xn = point
    # instead of computing the pow at every step, we will memorize the previously computed result
    # and multiply it by 'point'
    for i in range(0, len(coef)):
        res += xn * coef[i]
        xn *= point
    return modulo_p(res, p)


def compute_y(n, m):
    """
    Function for computing the encoding of input m as a vector y[] of size n.

    :param n: n = k + 2 * s
    :param m: input m represented as a vector of (k-1) Zp elements, where p is prime
    :return: y = (y1, y2, ..., yn) representing the encoding of input m
    """
    encoded_m = []
    for index in range(0, n):
        # P(1), P(2), ..., P(n):
        y_index = modulo_p(compute_polynomial(m, index + 1), p)
        # y_index = modulo_p(compute_polynomial_horner(m, index + 1), p)
        encoded_m.append(y_index)
    return encoded_m


print("------- m encoded as y[] -------")
y = compute_y(n, m)
print("y =", y)
