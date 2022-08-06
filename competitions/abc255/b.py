from math import sqrt, inf

n, k = map(int, input().split())
a = list(map(int, input().split()))

xys = []
for _ in range(n):
    xys.append(list(map(int, input().split())))

min_dist = 0
for i in range(n):
    tmp_min = inf
    if i + 1 in a:
        continue
    x, y = xys[i]
    for person_idx in a:
        l_x, l_y = xys[person_idx - 1]
        dist = (l_x - x) ** 2 + (l_y - y) ** 2
        if dist < tmp_min:
            tmp_min = dist
    if tmp_min > min_dist:
        min_dist = tmp_min

print(sqrt(min_dist))