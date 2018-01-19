# ro und r1 als Eingagbe für de EEA
def extgcd(r0, r1):
    u, v, s, t = 1, 0, 0, 1
    # Vertauschen wenn r1 < r0 ist
    if r1 < r0:
        temp = r1
        r1 = r0
        r0 = temp
    # Mit while schleife parameter berechnen
    while r1 != 0:
        q = r0//r1
        r0, r1 = r1, r0-q*r1
        u, s = s, u-q*s
        v, t = t, v-q*t
    return r0, u, v

def main():
    print("Geben sie r0 ein: ")
    r0 = int(input())
    print("Geben sie r1 ein: ")
    r1 = int(input())

    print("----- Ergebnis ----")

    a1, u1, v1 = extgcd(r0, r1)
    print(a1)
    print(u1)
    print(v1)

if __name__ == "__main__":
    main()