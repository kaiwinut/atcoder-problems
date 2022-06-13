## Explanation
n = int(input())
a = list(map(int, input().split()))

UPPER = 2 * 10 ** 5
cnt = [0] * (UPPER + 1)
for j in range(n):
    cnt[a[j]] += 1

# cnt[i] := |{j | a[j] <= i}|
for j in range(UPPER):
    cnt[j+1] += cnt[j]

ans = 0
for j in range(n):
    ans += cnt[a[j]-1] * (n - cnt[a[j]])  # num of indicies of As lesser than a[j] * num of indicies of As greater than a[j]
print(ans)

## TLE

# from itertools import combinations
# from collections import Counter
# n = int(input())
# a = list(map(int, input().split()))

# d = Counter(a)

# s = 0
# for c in list(combinations(list(d.values()), 3)):
#     s += c[0] * c[1] * c[2]

# print(s)