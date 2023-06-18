S = input()

nums = []
for i in range(len(S)-2):
    nums.append(int(S[i:i+3]))

min_diff = 10 ** 10
for n in nums:
    if abs(n - 753) < min_diff:
        min_diff = abs(n - 753)

print(min_diff)