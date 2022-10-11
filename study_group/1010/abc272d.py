from collections import deque
n,m = map(int, input().split())

directions = []
for i in range(n):
    for j in range(n):
        if i ** 2 + j ** 2 == m:
            directions.append((i, j))
            directions.append((-i, j))
            directions.append((i, -j))
            directions.append((-i, -j))

steps = [[-1] * n for _ in range(n)]
steps[0][0] = 0

q = deque()
q.append((0, 0))

while len(q) > 0:
    x, y = q.popleft()

    for d in directions:
        nsq = (x + d[0], y + d[1])
        if 0 <= nsq[0] < n and 0 <= nsq[1] < n and steps[nsq[0]][nsq[1]] == -1:
            steps[nsq[0]][nsq[1]] = steps[x][y] + 1
            q.append(nsq)

for s in steps:
    print(*s)