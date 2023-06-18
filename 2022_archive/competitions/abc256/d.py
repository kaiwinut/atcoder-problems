n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

lr.sort(key=lambda x: (x[0], x[1]))

x = -1
y = -1
for (l, r) in lr:
    if y != -1 and y < l:
        print(x,y)
        x = -1
        y = -1

    if x == -1:
        x = l
    if r > y:
        y = r

if x != -1 and y != -1:
    print(x,y)

## TLE

# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]

# nums = [0] * (2 * (10 ** 5) + 1)

# for (l, r) in lr:
#     nums = nums[:l] + [1] * (r-l) + nums[r:]

# sets = []
# x = -1
# y = -1
# for i in range(1, 2 * (10**5) + 1):
#     if x == -1 and nums[i] == 1:
#         x = i
#     if x != -1 and y == -1 and nums[i] == 0:
#         y = i
#         sets.append((x,y))
#         x = -1
#         y = -1

# for s in sets:
#     print(s[0], s[1])