n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_avg = sum(a)/len(a)
b_avg = sum(b)/len(b)

if a_avg == b_avg:
    print('same')

elif a_avg > b_avg:
    print('A')

else:
    print('B')