n = int(input())
b = list(map(int, input().split()))

a = []
b.append(b[-1])

# b1  b2  ...  bn-1 (bn)
# | \ | \      | \  | \
# a1 a2 a3   an-1 an

for i in range(len(b)-1, 0, -1):
    a.append(min(b[i], b[i-1]))
a.append(b[0])
print(sum(a))