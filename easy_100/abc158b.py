N, A, B = map(int, input().split())

a = A * (N // (A + B))
mod = N % (A+B)

if mod <= A:
    a += mod
else:
    a += A

print(a)