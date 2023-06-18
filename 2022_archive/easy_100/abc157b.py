A = []
for _ in range(3):
    A += list(map(int, input().split()))
N = int(input())
B = [int(input()) for _ in range(N)]

check = [0] * 9

mass = {}
for i, a in enumerate(A):
    mass[a] = i

for b in B:
    if b in mass.keys():
        check[mass[b]] = 1

r_1 = 0
r_2 = 0
r_3 = 0
c_1 = 0
c_2 = 0
c_3 = 0
d_1 = 0
d_2 = 0
for j in range(3):
    r_1 += check[j]
    r_2 += check[3+j]
    r_3 += check[6+j]
    c_1 += check[j*3]
    c_2 += check[j*3 + 1]
    c_3 += check[j*3 + 2]
    d_1 += check[j*4]
    d_2 += check[(j+1)*2]

if r_1 == 3 or r_2 == 3 or r_3 == 3 or c_1 == 3 or c_2 == 3 or c_3 == 3 or d_1 == 3 or d_2 == 3:
    print('Yes')
else:
    print('No')