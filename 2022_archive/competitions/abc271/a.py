n = int(input())
s = ''

x = n // 16
y = n % 16

d = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

print(d[x] + d[y])