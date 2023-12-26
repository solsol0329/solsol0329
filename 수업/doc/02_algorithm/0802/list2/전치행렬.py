'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1.
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for lst in arr:
    print(*lst)

#2.
for i in range(N):
    for j in range(i+1, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for lst in arr:
    print(*lst)

#3
print(list(zip(*arr)))

