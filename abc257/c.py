n = int(input())
S = input()
W = list(map(int, input().split()))

person = []
for s, w in zip(S, W):
    person.append([w, s])

person.sort(key=lambda x: (x[0],int(x[1])))

correct = [n]
for w, s in person:
    if s == '0':
        correct[0] -= 1

x = correct[-1]
for i in range(1, len(person)):
    x += 1 if person[i-1][1] == '0' else -1
    if person[i-1][0] != person[i][0]:
        correct.append(x)

correct.append(n - correct[0])

print(max(correct))