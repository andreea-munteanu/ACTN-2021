import random
from solovay_strassen import solovay_strassen
from lucas_lehmer import lucas_lehmer, mersenne_s

bits = 512

if __name__ == '__main__':
    p = 10 # Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    print(f'Random {bits}-bit Prime (p): ', p)
    print(f'Solovay-Strassen primality test (t = 80) for {p}: ', 'Prime' if solovay_strassen(p, 80) else 'Composite')
    s = random.randint(3, 16)
    print(f'Lucas-Lehmer primality test for M_{s} = {mersenne_s(s)}:', 'Prime' if lucas_lehmer(s) else 'Composite')


