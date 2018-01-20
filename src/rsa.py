from prime import *
import random

class RSA:
    n = 0
    d = 0
    e = 0

    def __init__(self, seed=42, lb=3, ub=100):
        self.n, self.d, self.e = generate_params(seed, lb, ub)

    def encryption(self, message):
        res = pow(message, self.e , self.n)
        return res

    def decryption(self, message):
        res = pow(message, self.d , self.n)
        return res

    def get_key_pub(self):
        return (n, e)

    def get_key_pr(self):
        return (n, d)