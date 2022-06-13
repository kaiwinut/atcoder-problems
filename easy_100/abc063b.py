S = input()

flag = True
seen = set()
for s in S:
    if s in seen:
        flag = False
        print('no')
        break
    else:
        seen.add(s)

if flag:
    print('yes')