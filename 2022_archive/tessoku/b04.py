n = input()
ans = 0

for i in range(len(n)):
    if n[len(n) - i - 1] == '1':
        ans += (1 << i)

print(ans)
