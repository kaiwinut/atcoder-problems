n = int(input())
T = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

t_sum = sum(T)

for (p, x) in px:
    new_sum = t_sum - T[p-1] + x
    print(new_sum)