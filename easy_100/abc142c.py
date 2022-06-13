N = int(input())
A = list(map(int, input().split()))

num = {}
for i, a in enumerate(A):
    num[a] = i + 1
A.sort()

ans = ' '.join([str(num[a]) for a in A])

print(ans)