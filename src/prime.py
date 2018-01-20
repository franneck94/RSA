import random
from math import sqrt
from euclid import *

# Function to test if a number is prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    for n in [3, 5, 7, 11, 13, 15, 17, 19]:
        if num % n == 0:
            return False
    for n in range(21, int(num * 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

# Function to generate random primes
def generate_primes(lb, ub):
    found = False

    while not found:
        p = random.randint(lb, ub)
        q = random.randint(lb, ub) 
        if is_prime(p) and is_prime(q) and p != q:
            found = True

    return p, q

# Function to compute e and d
def compute_params(phi_n):
    d = 0
    e = 0
    found_e = False

    while found_e == False:
        e = random.randint(1, phi_n - 1)
        if gcd(e, phi_n) == 1:
            found_e = True
    _, d, _ = extgcd(e, phi_n)
    if(d < 0):
        d += phi_n

    return d, e

# Main function to generate primes and params
def generate_params(seed=42, lb=3, ub=100, DEBUG=True):
    p, q = generate_primes(lb, ub)
    n = p * q 
    phi_n = (p-1) * (q-1)   
    d, e = compute_params(phi_n)
    if DEBUG == True:
        print("P, Q: ", p, q)
        print("N: ", n) 
        print("Phi(n): ", phi_n)  
        print("E, D: ", e, d)
    return n, d, e 