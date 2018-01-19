from prime import *
import random

class RSA:
    n = 0
    d = 0
    e = 0

    def __init__(self, n, d, e):
        self.n = n
        self.d = d
        self.e = e

    def encryption(self, message):
        return (message**self.d) % self.n

    def decryption(self, message):
        return (message**self.e) % self.n