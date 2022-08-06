k = int(input())
h = 21+k//60
t = k%60
if t < 10:
    s = '0' + str(t)
else:
    s = str(t)
print(str(h)+':'+s)