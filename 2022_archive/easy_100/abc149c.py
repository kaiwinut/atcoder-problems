X = int(input())

if X == 2 or X == 3:
    print(X)
else:
    while True:
        flag = True
        for i in range(2, X):
            if X % i == 0:
                flag = False
        if flag:
            print(X)
            break
        X += 1

## TLE

# if X == 2 or X == 3:
#     print(X)

# else:
#     primes = [2]

#     for i in range(3, X):
#         flag = True
#         for p in primes:
#             if i % p == 0:
#                 flag = False
#         if flag:
#             primes.append(i)

#     while True:
#         flag = True
#         for p in primes:
#             if X % p == 0:
#                 flag = False
#         if flag:
#             print(X)
#             break
#         X += 1