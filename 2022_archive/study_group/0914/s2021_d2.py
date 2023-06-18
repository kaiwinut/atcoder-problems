from math import factorial

p = int(input()) / 100

def c(a, b):
    return factorial(a) // (factorial(b) * factorial(a - b))

rate = c(7, 4) * (p ** 4 * (1 - p) ** 3) + c(7, 5) * (p ** 5 * (1 - p) ** 2) + c(7, 6) * (p ** 6 * (1 - p) ** 1) + c(7, 7) * (p ** 7 * (1 - p) ** 0)

print(f'{rate * 100:.12f}')