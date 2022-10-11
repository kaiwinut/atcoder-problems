import sys

n = int(input())
a = list(map(int,input().split()))

a.sort()

odd_sum = 0
c1 = 0
even_sum = 0
c2 = 0

if len(a) == 2 and (a[0] + a[1]) % 2== 1:
    print(-1)
    sys.exit()

for num in reversed(a):
    if num % 2 == 1 and c1 < 2:
        odd_sum += num
        c1 += 1
    if num % 2 == 0 and c2 < 2:
        even_sum += num
        c2 += 1

print(max(odd_sum, even_sum))