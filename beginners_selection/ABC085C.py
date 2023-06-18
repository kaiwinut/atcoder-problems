n,y = map(int,input().split())

flg = False
for i in range(n+1):
    for j in range(n+1):
        left = y - 10000 * i - 5000 * j
        k = n - i - j
        if left >= 0 and left % 1000 == 0 and left // 1000 == k:
            print(i,j,k)
            flg = True
            break
    if flg:
        break
if not flg:
    print(-1, -1, -1)