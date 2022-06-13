N, A, B = map(int, input().split())
S = input()

qual_cnt = 0
b_cnt = 0
for i, s in enumerate(S):
    if s == 'a' and qual_cnt < A + B:
        qual_cnt += 1
        print('Yes')
    elif s == 'b' and qual_cnt < A + B and b_cnt < B:
        qual_cnt += 1
        b_cnt += 1
        print('Yes')
    else:
        print('No')