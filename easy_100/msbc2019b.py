from math import ceil, floor

N = int(input())

x_low = N / 1.08
x_high = (N + 0.99999) / 1.08

if ceil(x_low) == floor(x_high):
    print(ceil(x_low))
else:
    print(':(')