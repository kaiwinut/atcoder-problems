N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

x_sum = 0
for a in A:
    x_sum += (D - 1) // a + 1

x_sum += X

print(x_sum)