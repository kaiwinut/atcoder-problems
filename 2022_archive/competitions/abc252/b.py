from sys import exit
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

max_a = max(a)
idx = []
for i in range(len(a)):
    if a[i] == max_a:
        idx.append(i+1)


for i in idx:
    if i in b:
        print('Yes')
        exit()

print('No')