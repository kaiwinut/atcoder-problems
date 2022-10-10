from itertools import accumulate

n = int(input())
tmp = bin(n)

bits = []
bit_ns = []

for i in range(len(tmp[2:])):
    if tmp[i+2] == '1':
        bits.append(len(tmp[2:]) - i - 1)

bits.reverse()

for j in range(len(bits)):
    bit_ns.append(2 ** bits[j])

b = len(bit_ns)

for i in range(1 << b):
    tmp = 0
    for j in range(b):
        if (1 << j) & i != 0:
            tmp += bit_ns[j]
    print(tmp)
