n = int(input())

s = ''
for i in range(10):
    s = str(n // (1 << i) % 2) + s

print(s)