a = [1, 2, 3, 4]
N = len(a)
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(a[i], a[j], a[k])
print('--------------------------------')
def comb(n, r, k, s): # s는 시작숫자
    if r == k:
        print(T)
    else:
        for i in range(s, n-r+1+k): # n-r+1 선택할 수 있는 마지막원소
            T[k] = a[i]
            comb(n, r, k+1, i+1)


a = [1, 2, 3, 4]
N = len(a)
R = 3
T = [0] * R
comb(N, R, 0, 0)