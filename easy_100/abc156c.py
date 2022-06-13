N = int(input())
X = list(map(int, input().split()))

# sum (p - x_i)^2
# sum p^2 - 2 p x_i + x_i^2
# -> min N p^2 - 2 p (x_i sum)

X.sort()
x_sq_sum = 0
x_sum = 0
for x in X:
    x_sq_sum += x ** 2
    x_sum += x

min_energy = 10 ** 10
for i in range(X[0], X[-1]+1):
    if N * i**2 - 2*i*x_sum + x_sq_sum < min_energy:
        min_energy = N * i**2 - 2*i*x_sum + x_sq_sum
print(min_energy)