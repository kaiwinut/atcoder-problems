from itertools import accumulate

n,q = map(int, input().split())
a = list(map(int, input().split()))

acc = list(accumulate(a))
acc = [0] + acc

for _ in range(q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l-1])