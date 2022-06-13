K, N = map(int, input().split())
A = list(map(int, input().split()))

dist = [A[-1] - A[0]]
for i in range(len(A)):
    dist.append(A[-i-1] - (A[-i] - K))

print(min(dist))