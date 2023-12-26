def H(n, r, k, s): # s는 시작숫자
    if r == k:
        print(T)
    else:
        for i in range(s, n): # n-r+1 선택할 수 있는 마지막원소
            T[k] = a[i]
            H(n, r, k+1, i)


a = [1, 2, 3, 4]
N = len(a)
R = 3
T = [0] * R
H(N, R, 0, 0)