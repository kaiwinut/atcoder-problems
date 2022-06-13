N, K = map(int, input().split())

N -= (N // K) * K

if N > K // 2:
    N = K - N

print(N)