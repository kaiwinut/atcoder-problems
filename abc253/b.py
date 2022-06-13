H, W = map(int, input().split())
S = [input() for _ in range(H)]

ij = []
for i, s in enumerate(S):
    for j, w in enumerate(s):
        if w == 'o':
            ij.append((i, j))

print(abs(ij[0][0] - ij[1][0]) + abs(ij[0][1] - ij[1][1]))