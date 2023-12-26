# [1, 2, 3] 모든 부분집합  2 ^ 3
def powerset(n, k):    # n: 원소의 갯수, k: 재귀의 깊이
    if n == k:
        print(bit)
    else:
        bit[k] = 1
        powerset(n, k+1)
        bit[k] = 0
        powerset(n, k+1)


arr =[1, 2, 3]
N = len(arr)
bit = [0] * N   # 원소의 포함 여부(0, 1)
powerset(N, 0)