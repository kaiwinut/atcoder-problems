n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

stages = {}
stage_time = [0]
for i, (a, b) in enumerate(ab):
    if (a, b) not in stages.keys():
        stages[(a,b)] = i+1
    stage_time.append(stage_time[-1] + a + b)

ab.sort(key=lambda x: (x[1], x[0]))

t = []
for (a, b) in ab:
    if stages[(a, b)] > x:
        continue
    time_to_stage = stage_time[stages[(a, b)]]
    t.append(time_to_stage + (x - stages[(a, b)]) * b)

print(min(t))