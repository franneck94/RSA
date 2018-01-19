import random
from euclid import *

def gcd(p, q):
    while q != 0:
        (p, q) = (q, p % q)
    return p

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def generate_primes():
    found = False

    while not found:
        p = random.randint(2, 100)
        q = random.randint(2, 100) 
        if is_prime(p) and is_prime(q) and p != q:
            found = True

    return p, q

def compute_params(phi_n):
    d = 0
    e = 0
    found_pair = False

    while not found_pair:
        e_candidate = random.randint(2, phi_n - 1)
        if gcd(e_candidate, phi_n) == 1:
            for d_candidate in range(1, phi_n):
                if gcd(d_candidate, phi_n) and d_candidate != e_candidate:
                    a, d_candidate, _ = extgcd(e_candidate, phi_n)
                    if a == 1:
                        found_pair = True
                        d = d_candidate
                        e = e_candidate

    return d, e

def generate_params(seed=42):
    p, q = generate_primes()
    print("P, Q: ", p, q)
    n = p * q 
    print("N: ", n)
    phi_n = (p-1) * (q-1)   
    print("Phi(n): ", phi_n)   
    d, e = compute_params(phi_n)
    print("D, E: ", d, e)

    return n, d, e 