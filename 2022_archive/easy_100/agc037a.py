S = input()

cnt = 0
curr = ''
prev = ''
for w in S:
    curr += w
    if curr != prev:
        cnt += 1
        prev = curr
        curr = ''
print(cnt)