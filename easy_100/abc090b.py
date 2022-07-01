A, B = map(int, input().split())

cnt = 0
for i in range(A, B+1):
    i_str = str(i)
    if i_str[0] == i_str[4] and i_str[1] == i_str[3]:
        cnt += 1

print(cnt)