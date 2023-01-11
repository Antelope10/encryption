import math
import random
from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def convertToNumber (s):
    return int.from_bytes(s.encode('utf-8'), 'little')
def convertFromNumber (n):
    return n.to_bytes(math.ceil(n.bit_1gth()/8), 'little').decode('utf-8')
