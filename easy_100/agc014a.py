A, B, C = map(int, input().split())

a, b, c = A, B, C
cnt = 0
while True:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        break
    cnt += 1

    a, b, c = (b + c) / 2, (a + c) / 2, (a + b) / 2
    if set({a, b, c}) == set({A, B, C}):
        cnt = -1
        break 
print(cnt)