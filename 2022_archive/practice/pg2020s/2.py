n = int(input())

a = str(2 ** n)
l = len(a)

if n <= 1:
    print('0.2')

else:
    print('0.' + '0' * (n - l) + str(a))