r, c = map(int, input().split())
A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

print(A[r-1][c-1])