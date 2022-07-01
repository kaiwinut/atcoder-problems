h1, h2, h3, w1, w2, w3 = map(int, input().split())

cnt = 0
for a1 in range(1, 31):
    for a2 in range(1, 31):
        for a4 in range(1, 31):
            for a5 in range(1, 31):
                a3 = h1 - a1 - a2
                a6 = h2 - a4 - a5
                a7 = w1 - a1 - a4
                a8 = w2 - a2 - a5
                if h3 - a7 - a8 == w3 - a3 - a6 and 30 >= h3 - a7 - a8 > 0 and a3 > 0 and a6 > 0 and a7 > 0 and a8 > 0:
                    cnt += 1

print(cnt)