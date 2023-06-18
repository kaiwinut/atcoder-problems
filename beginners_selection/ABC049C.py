s = input()

i = len(s)
while True:
    if s[i-5:i] == 'dream' and i >= 5:
        i -= 5
    elif s[i-7:i] == 'dreamer' and i >= 7:
        i -= 7
    elif s[i-5:i] == 'erase' and i >= 5:
        i -= 5
    elif s[i-6:i] == 'eraser' and i >= 6:
        i -= 6
    else:
        break

print('NO' if i > 0 else 'YES')
