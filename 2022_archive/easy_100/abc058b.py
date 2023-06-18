o = input()
e = input()

s=''
for i in range(len(e)):
    s += o[i] + e[i]

if len(o) > len(e):
    s += o[-1]

print(s)