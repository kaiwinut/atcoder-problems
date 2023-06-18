from bisect import bisect_left

n,x = map(int,input().split())
a = list(map(int,input().split()))

print(bisect_left(a, x) + 1)