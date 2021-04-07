import random


def modular_exponentiation(a, n, m):  # works; checked
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

#
# # Python program to find (a^b) mod m for a large 'a'
# def aModM(s, m):
#     number = 0
#
#     # convert string s[i] to integer which gives
#     # the digit value and form the number
#     for i in range(len(s)):
#         number = (number * 10 + int(s[i]))
#         number = number % m
#
#     return number
#
#
# # Returns find (a^b) % m
# def ApowBmodM(a, b, m):
#     # Find a%m
#     ans = aModM(a, m)
#     mul = ans
#
#     # now multiply ans by b-1 times and take
#     # mod with m
#     for i in range(1, b):
#         ans = (ans * mul) % m
#
#     return ans


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


def solovay_strassen(n, t) -> bool:
    """
    Solovay-Strassen probabilistic primality test.

    Accuracy: If the input n is indeed prime, then the output will always correctly be probably prime. However,
    if the input n is composite then it is possible for the output to be incorrectly probably prime.
    The number n is then called an Euler–Jacobi pseudo-prime.

    :param n: odd integer n ≥ 3
    :param t: security parameter t ≥ 1 (number of iterations)
    :return: true if n is prime, false otherwise
    """
    for i in range(0, t):
        # choose a at random s.t. 2 ≤ a ≤ n - 2:
        a = random.randint(2, n - 1)
        # compute r = (a ** ((n-1)/2)) mod n:
        r = modular_exponentiation(a, (n-1)//2, n)
        # r = pow(a, (n-1)//2, n)
        # if r != 1 and r!= n-1 --> n is composite
        if r not in [1, n-1]:
            return False
        # compute the Jacobi symbol s = (a/n)
        s = jacobi(a, n)
        # if r !≡ s mod n, then n is composite
        if r != s % n:
            return False
    return True  # probably prime


