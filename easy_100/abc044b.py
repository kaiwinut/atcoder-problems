w = input()

seen = {chr(ord('a')+i):0 for i in range(26)}

for s in w:
    seen[s] += 1

flag = True
for k, v in seen.items():
    if v % 2 == 1:
        print('No')
        flag = False
        break

if flag:
    print('Yes')