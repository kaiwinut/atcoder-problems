N = int(input())

for i in range(8):
    if 2 ** i > N:
        print(2 ** (i-1))
        break
    elif 2 ** i == N:
        print(2 ** i)
        break