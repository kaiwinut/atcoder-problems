S = input()

while True:
    if S[-5:] == 'dream' or S[-5:] == 'erase':
        S = S[:-5]
    elif S[-6:] == 'eraser':
        S = S[:-6]
    elif S[-7:] == 'dreamer':
        S = S[:-7]
    else:
        print('NO')
        break

    if len(S) == 0:
        print('YES')
        break