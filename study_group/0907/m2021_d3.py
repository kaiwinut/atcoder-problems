import sys
x = input()

for i in range(len(x)):
    if x[i] == '0':
        print(x[:i] + '1' + '1' * (len(x) - i - 1))
        sys.exit()

print(x)