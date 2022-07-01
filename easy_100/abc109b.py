import sys
from collections import Counter
n = int(input())
ws = [input() for _ in range(n)]

last_word = ws[0]
d = Counter()
d[last_word] += 1
for w in ws[1:]:
    d[w] += 1
    if w[0] != last_word[-1] or d[w] >= 2:
        print('No')
        sys.exit()
    last_word = w
print('Yes')