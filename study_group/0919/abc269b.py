s = [input() for _ in range(10)]

a = 0
b = 0
c = 0
d = 0

for i in range(len(s)):
    for j in range(len(s[i])):
        if a == 0 and s[i][j] == '#':
            a = i + 1
            c = j + 1
        elif a != 0 and s[i][j] == '#':
            b = i + 1
            d = j + 1

if b == 0:
    b = a

if d == 0:
    d = c

print(a, b)
print(c, d)