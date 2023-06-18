n, q = map(int, input().split())
S = input()
queries = [map(int, input().split()) for _ in range(q)]

pos = 0
for i, x in queries:
    if i == 2:
        j = x - pos
        j += -(j//n) * n
        print(S[j - 1])
    else:
        pos += x