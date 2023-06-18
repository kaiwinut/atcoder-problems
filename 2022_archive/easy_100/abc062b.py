h,w = map(int, input().split())
a = [input() for _ in range(h)]

print('#'*(len(a[0])+2))
for ra in a:
    print('#' + ra + '#')
print('#'*(len(a[0])+2))