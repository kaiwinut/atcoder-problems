import sys

n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if a[i] + a[j] + a[k] == 1000 and i != j and i!= k and j != k:
                print('Yes')
                sys.exit()

print('No')