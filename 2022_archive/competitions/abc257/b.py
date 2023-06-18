n,k,q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

mass = [0] * (n+1)
koma = [0] + [a for a in A]

for a in A:
    mass[a] = 1

for l in L:
    if koma[l] >= n:
        continue
    elif mass[koma[l]] == 1 and mass[koma[l]+1] == 0:
        mass[koma[l]] = 0
        mass[koma[l]+1] = 1
        koma[l] = koma[l] + 1

lst = []
for i, m in enumerate(mass):
    if m == 1:
        lst.append(str(i))

print(' '.join(lst))