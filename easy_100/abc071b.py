S = input()

seen = set()
for s in S:
    seen.add(s)

flag = False
for i in range(26):
    if chr(ord('a') + i) not in seen:
        flag = True
        print(chr(ord('a') + i))
        break

if not flag:
    print('None')