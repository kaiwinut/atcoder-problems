N, M, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = M
while left <= right:
    mid = (left + right) // 2
    if A[mid] == X:
        break
    elif A[mid] < X:
        left = mid + 1
    elif A[mid] > X:
        right = mid - 1

print(min(left, M - left))

## Using bisect

# from bisect import bisect_right

# idx = bisect_right(A, X)
# print(min(idx, M - idx))