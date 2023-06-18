n = int(input())

s = ''
for i in range(10):
    if (n // (1 << i)) % 2 == 1:
        s = '1' + s
    else:
        s = '0' + s

print(s)