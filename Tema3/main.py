import random
from solovay_strassen import solovay_strassen
from lucas_lehmer import lucas_lehmer, mersenne_s, check_prime


# list of primes for p (solovay-strassen):
# 131071, 999999000001, 170141183460469231731687303715884105727 = M_127,
# 5210644015679228794060694325390955853335898483908056458352183851018372555735221,
# 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151


# list of primes for s (lucas-lehmer):
# 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279 etc.


if __name__ == '__main__':
    bits = 512
    p = 0
    # only run solovay-strassen for odd numbers:
    while p % 2 == 0:
        p = random.getrandbits(bits)

    """ ___________________________________________ SOLOVAY-STRASSEN ________________________________________________"""

    file = open(f'solovay_strassen_res.txt', "w+")
    primes = [7, 15, 17, 19, 23, 29, 43, 47, 59, 61, 97, 99, 101, 103, 9349, 131071, 131075, 3010349,
              54018521, 370248451, 6643838879, 999999000001, 99999900000707,
              3331113965338635107, 6161791591356884791277, 170141183460469231731687303715884105727,
              982522283828175956912680736200429527560213, 55152514369611148024937646637560831269227779560863,
              4451428565034150528420364724658759582595522477635407755377648676948917710018929680756030707498769587]
    for p in primes:
        print(f'{p}: ', 'Prime' if solovay_strassen(p, 80) else 'Composite', sep='', file=file)

    # print(f'Solovay-Strassen for {p}: ', 'Prime' if solovay_strassen(p, 80) else 'Composite', sep='', file=file)
    # primes = [131071, 131075, 999999000001, 99999900000707, 170141183460469231731687303715884105727]
    # for p in primes:
    #     print(f'Solovay-Strassen for {p}: ', 'Prime' if solovay_strassen(p, 80) else 'Composite', sep='', file=file)

    """ _____________________________________________ LUCAS-LEHMER __________________________________________________"""

    file = open(f'lucas_lehmer_res.txt', "w+")
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61]
    for s in primes:
        print(f'M_{s} = {mersenne_s(s)}: ', 'Prime' if lucas_lehmer(s) else 'Composite',
              sep='', file=file)
    # print(f'\nRandom {bits}-bit prime p: ', p)
    # t = 80
    # print(f'Solovay-Strassen primality test (t = {t}) for p: ', 'Prime' if solovay_strassen(p, t) else 'Composite')
