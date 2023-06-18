n,a,b = map(int, input().split())

def isok(i):
    tmp = i
    lst = [0] * 10
    for j in range(len(lst)):
        lst[j] = tmp % 10
        tmp //= 10
    return a <= sum(lst) <= b

s = 0
for i in range(1, n+1):
    if isok(i):
        s += i

print(s)