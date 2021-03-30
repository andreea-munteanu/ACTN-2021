import random
from solovay_strassen import solovay_strassen
from lucas_lehmer import lucas_lehmer, mersenne_s, check_prime


# list of primes for p:
# 131071, 999999000001, 170141183460469231731687303715884105727 = M_127,
# 5210644015679228794060694325390955853335898483908056458352183851018372555735221,
# 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151


# list of primes for s:
# 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279 etc.


if __name__ == '__main__':
    bits = 512
    p = 0
    # only run solovay-strassen for odd numbers:
    while p % 2 == 0:
        p = random.getrandbits(bits)
    print(f'\nRandom {bits}-bit Prime (p): ', p)
    print(f'Solovay-Strassen primality test (t = 80) for p: ', 'Prime' if solovay_strassen(p, 60) else 'Composite')
    s = 0
    while not check_prime(s):
        s = random.randint(10, 40)
    print("\ns =", s)
    print(f'Lucas-Lehmer primality test for M_{s} = {mersenne_s(s)}:', 'Prime' if lucas_lehmer(s) else 'Composite')

