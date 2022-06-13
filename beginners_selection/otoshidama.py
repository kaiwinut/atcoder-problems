N, Y = map(int, input().split())

c = Y // 1000
if c == N:
    print(0, 0, c)

elif c < N:
    print(-1, -1, -1)

else:
    flag = False
    for a in range(N+1):
        for b in range(N+1-a):
            c_after = c - 5 * b - 10 * a
            if a + b + c_after == N and c_after >= 0:
                flag = True
                print(a, b, c_after)
                break
        if flag:
            break
    if flag == False:
        print(-1, -1, -1)