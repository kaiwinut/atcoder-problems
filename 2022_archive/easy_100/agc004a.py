A, B, C = map(int, input().split())

if A * B * C % 2 == 0:
    print(0)
else:
    print(min(A*B, B*C, A*C))