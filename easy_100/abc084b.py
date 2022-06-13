A, B = map(int, input().split())
S = input()

if '-' not in S:
    print('No')

else:
    s = S.split('-')

    if len(s) != 2:
        print('No')

    elif not s[0].isnumeric() or not s[1].isnumeric():
        print('No')

    elif len(s[0]) != A or len(s[1]) != B:
        print('No') 

    else:
        print('Yes')