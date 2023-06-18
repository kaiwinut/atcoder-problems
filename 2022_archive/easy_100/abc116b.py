s = int(input())

A = [s]
seen = set({s})

for m in range(2, 10 ** 6 + 1):
    a_next = A[-1] // 2 if A[-1] % 2 == 0 else 3 * A[-1] + 1
    if a_next in seen:
        print(m)
        break
    else:
        seen.add(a_next)
        A.append(a_next)