N = int(input())
P = [(0, 0, 0)]
for _ in range(N):
    P.append(tuple(map(int, input().split())))

flag = True
for i in range(len(P) - 1):
    t_next, x_next, y_next = P[i+1]
    t, x, y = P[i]
    dist = abs(x_next - x) + abs(y_next - y)
    if (t_next - t - dist) % 2 != 0 or dist > t_next - t:
        flag = False
        print('No')
        break

if flag:
    print('Yes')