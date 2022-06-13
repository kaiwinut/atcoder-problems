n = int(input())

s = 0
for i in range(1,10):
    for j in range(1, 10):
        s += i*j

a = s - n

for i in range(1, a+1):
    if a % i == 0 and i <= 9 and a//i <=9:
        print(str(i) + ' x ' + str(a//i))