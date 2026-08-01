def gf256_multiply(a, b):
    result = 0

    while b:
        if b & 1:
            result ^= a
        a   = a << 1
        if a & 0x100:
            a ^= 0x11D
        b = b >> 1
        print(a)
    return result

print(gf256_multiply(1, 30))