N = int(input())
A = list(map(int, input().split()))

cnt = 0
flag = True
while flag:
    for a in A:
        if a % (2 ** (cnt+1)) != 0:
            flag = False
    if flag:
        cnt += 1
print(cnt)