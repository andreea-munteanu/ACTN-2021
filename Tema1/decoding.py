"""
• Suppose that the input z has at most s errors (i.e., |{i ∈ {1,...,n}|zi =
yi}| ≤ s -thus, |{i ∈ {1,...,n}|zi = yi}| ≥ k + s);
• Generate A ⊂ {1,...,n}, with |A| = k, and compute the free coefficient.

If the free coefficient is 0, compute P(x).
"""

from encoding import n, y, s, p, k, modulo_p
import random
import itertools


def get_z_and_A():
    """
    Function for getting vector z s.t. z[i] = y[i] for i = 1, 2, ..., n except for s positions.

    :return: vector z
    """
    z = y                                       # initially, z[i] = y[i] for all i = 1, 2, ..., n
    pos = [x for x in range(0, n)]
    A = pos                                     # A will contain all indexes where z[i] = y[i] holds
    positions_to_change = []                    # positions already set to be changed
    for i in range(0, s):                       # there will be s positions changed in vector y
        taken_pos = random.choice(pos)
        # print("taken_pos =", taken_pos)
        if taken_pos not in positions_to_change:
            positions_to_change.append(taken_pos)
            initial_val = z[taken_pos]
            while initial_val == z[taken_pos]:  # making sure we insert error by repetition
                z[taken_pos] = random.randint(0, p)
            A.remove(taken_pos)                 # remove from A positions where errors occur
        else:
            i -= 1
    return z, A


print("------- vectors z and A --------")
z, A = get_z_and_A()
print("z =", z, "\nA =", A)


# def generate_subsets_of_size_k(A, k):
#     """
#     Method for determining subsets of size k of vector A.
#
#     :return: list of lists containing all subsets of size k for vector A
#     """
#     subsets = list(itertools.combinations((A), k))
#     list_subsets = []
#     for sub in subsets:
#         sub = list(sub)
#         list_subsets.append(sub)
#     return list_subsets
#
#
# subsets = generate_subsets_of_size_k(A, k)
# print("subsets: ", subsets)


def modulo_inverse(a, p):
    """
    Method for computing the modulo inverse of a number a in modulo p .

    :param a: number for which we make the computation
    :return: a ** (-1) in modulo p
    """
    return pow(a, -1, p)


def modulo_subtraction(a, b, p):
    """
    Method for computing modular subtraction: (a-b) mod c = (a mod c - b mod c) mod c

    :param a:
    :param b:
    :param p:
    :return: subtraction (a-b) in modulo p
    """
    return modulo_p(modulo_p(a, p) - modulo_p(b, p), p)


def compute_fc(A, z):
    """
    Method for computing the free coefficient.

    :param A: our set
    :return: fc (should be 0).
    """
    fc = 0  # the free coefficient we will return as output
    for i in A:
        prod = 1
        for j in A:
            if j != i:
                # should be j and i, but we indexed our vectors from 0:
                prod *= (j + 1) * modulo_inverse(modulo_subtraction(j + 1, i + 1, p), p)
        fc += z[i] * prod
    # result is in Z(p):
    return modulo_p(fc, p)


print("------- free coefficient -------")
free_coefficient = compute_fc(A, z)
print("fc =", free_coefficient)


def compute_P_in_point(A, x):
    """
    Method for computing P(X) in a given point x for when fc = 0.

    :param A: set of indices
    :param x: point in which we compute the polynomial
    :return: value of P(x) in modulo p
    """
    val = 0
    for i in A:
        prod = 1
        for j in A:
            if i != j:
                # should be j and i, but we indexed our vectors from 0:
                prod *= modulo_subtraction(x, j + 1, p) * modulo_inverse(modulo_subtraction(i + 1, j + 1, p), p)
        val += modulo_p(z[i] * prod, p)
    return modulo_p(val, p)









