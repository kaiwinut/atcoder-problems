import sys
a = input()
b = input()

if len(a) > len(b):
    print('GREATER')
elif len(a) < len(b):
    print('LESS')
else:
    for sa, sb in zip(a, b):
        if int(sa) > int(sb):
            print('GREATER')
            sys.exit()
        elif int(sa) < int(sb):
            print('LESS')
            sys.exit()
    print('EQUAL')