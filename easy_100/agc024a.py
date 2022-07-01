a,b,c,k = map(int, input().split())

# 0th a-b
# 1st (a+b+c-a), (a+b+c-b), (a+b+c-c)  b-a
# -> 2nd (a + b + c) + a, (a + b + c) + b, (a + b + c) + c,  a-b
# -> 3rd 2(a+b+c) +b+c, 2(a+b+c) +a+c, 2(a+b+c) +a+b   b-a
# -> 4th __ + 2a+b+c, a+2b+c, ..  a-b
# -> 5th b-a

if abs(b-a) > 10 ** 18:
    print('Unfair')
else: 
    i = -1 if k % 2 == 1 else 1
    print(i*(a-b))