from rsa import RSA

def main():
    x = 97
    y = -1

    rsa = RSA(seed=42, lb=1001, ub=10000)
    print('Original message: ', x)
    y = rsa.encryption(x)
    print('Encrypted message: ', y)
    x = rsa.decryption(y)
    print('Decrypted message: ', x)

if __name__ == "__main__":
    main()