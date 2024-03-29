from collections import defaultdict

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


uf = UnionFind(len(xy))

def is_conn(x, y):
    if [x[0] - 1, x[1] - 1] == y:
        return True
    if [x[0] - 1, x[1]] == y:
        return True
    if [x[0], x[1] - 1] == y:
        return True
    if [x[0], x[1] + 1] == y:
        return True
    if [x[0] + 1, x[1]] == y:
        return True
    if [x[0] + 1, x[1] + 1] == y:
        return True
    return False

for i in range(len(xy)):
    for j in range(i+1, len(xy)):
        if is_conn(xy[i], xy[j]):
            uf.union(i, j)
            # print(i, j)
            # print(uf.parents)

# print(uf.parents)
# print(uf.all_group_members())
print(uf.group_count())