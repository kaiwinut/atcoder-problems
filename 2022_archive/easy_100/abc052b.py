N = int(input())
S = input()

x = 0
accum = [x]
for s in S:
    x += 1 if s == 'I' else -1
    accum.append(x)

print(max(accum))