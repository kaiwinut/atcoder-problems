x, a, d, n = map(int, input().split())

## Explanation

if d < 0:
    a = a + d * (n - 1)
    d = -d

if x < a:
    print(a - x)

elif x > a + d * (n - 1):
    print(x - a - d * (n - 1))

else:
    if d == 0:
        print(0)
    else:
        mod = (x - a) % d
        print(min(mod, d - mod))


## WA

# x = x - a
# if d < 0:
#     x = -x
#     d = -d

# if x <= 0 or d == 0:
#     print(abs(x))

# elif x >= n * d:
#     print(x - n * d)

# else:
#     mod = x % d
#     print(min(mod, d - mod))

## WA

# if d == 0:
#     print(abs(x-a))

# elif d > 0 and a + d * (n-1) < x:
#     print(x - a - d * (n-1))

# elif d < 0 and a + d * (n-1) < x:
#     print(x - a)

# elif d < 0 and a + d * (n-1) > x:
#     print(a + d * (n-1) - x)

# elif d > 0 and a > x:
#     print(a - x)

# else:
#     mod = (x - a) % d
#     print(min(abs(d-mod), abs(mod)))