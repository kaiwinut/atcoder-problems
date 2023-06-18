N, K = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(a)

flag = True
for i in range(K):
    idx = i
    pa = []
    pb = []
    while idx <= N - 1:
        pa.append(a[idx])
        pb.append(b[idx])
        idx += K

    if sorted(pa) != pb:
        print('No')
        flag = False
        break

if flag:
    print('Yes')