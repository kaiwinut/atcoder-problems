n = int(input())
a = [0] + list(map(int, input().split()))

p = [0] * (n+2)  # 1~i番目の部屋までの最大人数 (先頭から)
q = [0] * (n+2)  # i~n番目の部屋までの最大人数 (後尾から: n~iで考えた方が考えやすい)
for i in range(1, len(a)):
    p[i] = max(p[i-1], a[i])

for i in reversed(range(1, len(a))):
    q[i] = max(q[i+1], a[i])

d = int(input())
for _ in range(d):
    l, r = map(int, input().split())
    print(max(p[l-1], q[r+1]))