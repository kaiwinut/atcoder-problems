import queue


n = int(input())
A = [input() for _ in range(n)]
B = []

max_nums = []

for _ in range(3):
    for a in A:
        b = a * 3
        B.append(b)

starts = []
for num in reversed(range(1, 10)):
    for i in range(n):
        for j in range(n):
            if A[i][j] == str(num):
                starts.append((n+i,n+j))
    if len(starts) > 0:
        break

direction = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

for i, j in starts:
    for d in direction:
        s = ''
        for k in range(n):
            s += B[i+d[0]*k][j+d[1]*k]
        max_nums.append(int(s))

print(max(max_nums))