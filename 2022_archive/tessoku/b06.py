from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(len(a)):
    if a[i] == 0:
        a[i] = -1

acc = list(accumulate(a))
acc = [0] + acc

for _ in range(q):
    l, r = map(int, input().split())
    s = acc[r] - acc[l-1]
    if s == 0:
        print('draw')
    elif s > 0:
        print('win')
    else:
        print('lose')