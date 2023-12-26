'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 체크
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj])

