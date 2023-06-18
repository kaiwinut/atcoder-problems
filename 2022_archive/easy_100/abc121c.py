N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

p_to_n = {}
for ab in AB:
    p, n = ab
    if p not in p_to_n.keys():
        p_to_n[p] = n
    else:
        p_to_n[p] += n

sorted_price = sorted(list(p_to_n.keys()))

ttp = 0
for p in sorted_price:
    if M <= p_to_n[p]:
        ttp += M * p
        break
    else:
        ttp += p_to_n[p] * p
        M -= p_to_n[p]

print(ttp)