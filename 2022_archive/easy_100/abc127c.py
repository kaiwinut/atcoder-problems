N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

max_l = 1
min_r = N

for lr in LR:
    l, r = lr
    if l > max_l:
        max_l = l
    if r < min_r:
        min_r = r
    if min_r < max_l:
        break

if min_r < max_l:
    print(0)
else:
    print(min_r - max_l + 1)

## TLE

# N, M = map(int, input().split())
# LR = [list(map(int, input().split())) for _ in range(M)]

# card_gate = {i: set() for i in range(1, N+1)}
# for m in range(M):
#     for n in range(LR[m][0], LR[m][1] + 1):
#         card_gate[n].add(m)

# cnt = 0
# for card in card_gate.keys():
#     if len(card_gate[card]) == M:
#         cnt += 1

# print(cnt)