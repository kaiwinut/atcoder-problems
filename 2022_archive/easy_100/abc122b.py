S = input()

lengths = [0]
for s in S:
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        lengths[-1] += 1
    else:
        lengths.append(0)

print(max(lengths))