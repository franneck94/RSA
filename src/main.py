from rsa import *
from prime import *

def main():
    x = 12
    y = -1

    n, d, e = generate_params(seed=42)
    rsa = RSA(n, d, e)
    print('Original message: ', x)
    y = rsa.encryption(x)
    print('Encrypted message: ', y)
    x = rsa.decryption(y)
    print('Decrypted message: ', x)

if __name__ == "__main__":
    main()