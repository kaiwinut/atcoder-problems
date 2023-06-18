from collections import Counter

s = input()

d = Counter()
for w in s:
    d[w] += 1

if d['N'] * d['S'] == 0 and d['N'] + d['S'] > 0:
    print('No')
elif d['E'] * d['W'] == 0 and d['E'] + d['W'] > 0:
    print('No')
else:
    print('Yes')