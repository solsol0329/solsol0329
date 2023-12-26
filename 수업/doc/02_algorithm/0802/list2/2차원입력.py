'''
3 4
1 2 3 4
5 6 7 9
9 10 11 12
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr = [list(map(int, input())) for _ in range(N)]  # 숫자가 붙어 있을 때

# 행우선 -
# for i in range(N):   # len(arr)
#     for j in range(M):  # len(arr[i])
#         print(arr[i][j])

# 열우선
# for j in range(M):  # len(arr[i])
#     for i in range(N):   # len(arr)
#         print(arr[i][j])

# 단, 정방행렬일 때 가능
# for i in range(N):   # len(arr)
#     for j in range(M):  # len(arr[i])
#         print(arr[j][i])

# 행의 합
sum_all = 0
for i in range(N):   # len(arr)
    sum_row = 0
    for j in range(M):  # len(arr[i])
        sum_all += arr[i][j]
        sum_row += arr[i][j]
    # 행은 합은 여기서 작업
    print(sum_row)
print(sum_all)

# 열의 합
sum_all = 0
for j in range(M):  # len(arr[i])
    sum_col = 0
    for i in range(N):  # len(arr)
        sum_all += arr[i][j]
        sum_col += arr[i][j]
    # 행은 합은 여기서 작업
    print(sum_col)
print(sum_all)