import sys
n,m = map(int, input().split())

c = {}
members = [i for i in range(1, n+1)]

for i in range(m):
    inputs = list(map(int, input().split()))
    k = inputs[0]
    inputs = inputs[1:]    
    for j in range(len(inputs)):
        for l in range(len(inputs)):
            if (inputs[j], inputs[l]) not in c:
                c[(inputs[j], inputs[l])] = 1
            else:            
                c[(inputs[j], inputs[l])] += 1
            if (inputs[l], inputs[j]) not in c:
                c[(inputs[l], inputs[j])] = 1
            else:            
                c[(inputs[l], inputs[j])] += 1

for a in members:
    for b in members:
        if (a, b) not in c:
            # print(c)
            # print(members)
            # print(a,b)
            print('No')
            sys.exit()

print('Yes')