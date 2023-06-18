import math

t = int(input())
nm = [list(map(int, input().split())) for _ in range(t)]

for n, m in nm:
    if m == 0:
        print(n, n)
    else:
        N = int(math.sqrt(2 * m))
        print(n-m if n > m else 1, n-N if N < math.sqrt(2 * m) else n-N+1)


"""
N * (N-1) // 2 = N ** 2 // 2 - N // 2
(N+1) * N // 2 = N ** 2 // 2 + N // 2

(N-1) ** 2 // 2 = N ** 2 // 2 - N // 2 + 1 // 2

N ** 2 // 2 - N // 2 <= m < N ** 2 // 2 + N // 2
sqrt(N ** 2 - N) <= sqrt(2m) < sqrt(N ** 2 + N)

max: 
"""