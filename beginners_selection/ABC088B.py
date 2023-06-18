n = int(input())
al = list(map(int, input().split()))

al.sort(reverse=True)

s = 0
for i, a in enumerate(al):
    s += (-a if i % 2 else a)

print(s)
