import sys
S = input()

if S[0] != 'A':
    print('WA')
    sys.exit()

cnt = 0
for s in S[2:-1]:
    if s == 'C':
        cnt += 1

if cnt != 1:
    print('WA')
    sys.exit()

for s in S:
    if s != 'A' and s != 'C' and s.isupper():
        print('WA')
        sys.exit()

print('AC')