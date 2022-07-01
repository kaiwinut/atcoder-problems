from hashlib import new


x = int(input())

ans = 1
for i in range(2, x+1):
    new_i = i*i
    while new_i <= x:
        ans = max(ans, new_i)
        new_i *= i
print(ans)