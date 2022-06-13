n, q = map(int, input().split())
nums = list(map(int, input().split()))

# O(NlogN)
nums.sort()

# O(N)
accum = []
for num in nums:
    if len(accum) == 0:
        accum.append(num)
    else:
        accum.append(accum[-1] + num)
accum.append(0)

# O(q * logN)
steps = []
for _ in range(q):
    num_q = int(input())
    top = len(nums) - 1
    bot = 0
    while bot <= top:
        mid = (top + bot) // 2
        if nums[mid] < num_q:
            bot = mid + 1
        else:
            top = mid - 1
    
    lower_sum = bot * num_q - accum[bot - 1]
    upper_sum = accum[n - 1] - accum[bot - 1] - (n - bot) * num_q
    print(lower_sum + upper_sum)

## TLE

# n, q = map(int, input().split())
# nums = list(map(int, input().split()))

# s = []
# for _ in range(q):
#     steps = 0
#     num_q = int(input())
#     for num in nums:
#         steps += abs(num - num_q)
#     s.append(steps)

# for step in s:
#     print(step)