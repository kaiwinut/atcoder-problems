from bisect import bisect_right
n = int(input())
a = list(map(int,input().split()))

sorted_a = sorted(list(set(a)))
nums = {}

for i in range(n):
    index = bisect_right(sorted_a, a[i])
    key = len(sorted_a) - index
    if key not in nums:
        nums[key] = 1
    else:
        nums[key] += 1

for i in range(n):
    if i in nums:
        print(nums[i])
    else:
        print(0)
