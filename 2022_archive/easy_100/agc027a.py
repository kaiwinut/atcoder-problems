N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
accum = []
for a in A:
    if len(accum) == 0:
        accum.append(a)
    else:
        accum.append(accum[-1] + a)

for k in range(len(accum)):
    if accum[k] > x:
        print(k)
        break
    elif accum[k] == x:
        print(k+1)
        break
    if k == N - 1:
        print(k)