s = input()

A_pos = -1
Z_pos = -1
for i, w in enumerate(s):
    if w == 'A' and A_pos == -1:
        A_pos = i
    if w == 'Z':
        Z_pos = i

print(Z_pos - A_pos + 1)