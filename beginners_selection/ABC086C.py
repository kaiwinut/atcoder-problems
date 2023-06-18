n = int(input())
txy = [list(map(int,input().split())) for _ in range(n)]

flg = False
pt,px,py = 0,0,0
for t,x,y in txy:
    dt = t - pt
    dx = abs(x - px)
    dy = abs(y - py)

    if not (dt >= dx + dy and (dt - dx - dy) % 2 == 0):
        flg = True
        break

    pt,px,py = t,x,y

print('No' if flg else 'Yes')