a,b,k = map(int,input().split())

seen = set()
for i in range(k):
    if a+i <= b:
        print(a+i)
        seen.add(a+i)
for i in reversed(range(k)):
    if b-i not in seen and b-i >= a:
        print(b-i)