from collections import deque

h,w = map(int,input().split())
px,py,qx,qy = map(int,input().split())
s = [input() for _ in range(h)]

d = {
    'U': [(0, -1), (-1, 0), (0, 1), (1, 0)],
    'R': [(-1, 0), (0, 1), (1, 0), (0, -1)],
    'D': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    'L': [(1, 0), (0, -1), (-1, 0), (0, 1)],
}

turn = {(0, -1): 'L', (-1, 0): 'U', (0, 1): 'R', (1, 0): 'D'}

seen = [[{'U': False, 'R': False, 'D': False, 'L': False} for _ in range(w)] for _ in range(h)]

cnt = 0
q = deque()
q.append((px - 1, py - 1, 'U'))

while q:
    cx, cy, face = q.popleft()
    if cx == qx - 1 and cy == qy - 1:
        print(cnt)
        exit()
    if seen[cx][cy][face]:
        print(-1)
        exit()
    seen[cx][cy][face] = True
    for di in d[face]:
        if 0 <= cx + di[0] < h and 0 <= cy + di[1] < w and s[cx + di[0]][cy + di[1]] == '.':
            q.append((cx + di[0], cy + di[1], turn[di]))
            cnt += 1
            break

print(-1)