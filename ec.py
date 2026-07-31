def gf256_multiply(a, b):
    xor = a ^ b
    return xor

print("xor result of 6 & 7:")
print(gf256_multiply(6, 7))