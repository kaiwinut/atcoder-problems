S = input()

n_start_with_one = 0
n_start_with_zero = 0

for i, s in enumerate(S):
    if (s == '0' and i % 2 == 0) or (s == '1' and i % 2 == 1):
        n_start_with_one += 1
    if (s == '1' and i % 2 == 0) or (s == '0' and i % 2 == 1):
        n_start_with_zero += 1

print(min(n_start_with_one, n_start_with_zero))