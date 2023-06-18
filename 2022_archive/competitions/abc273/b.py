x,k=map(int, input().split())

for i in range(k):
    n = (x // (10 ** i)) % 10
    if n >= 5:
        x += (10 ** (i+1)) - n * (10 ** i)
    else:
        x -= n * (10 ** i)

print(x)