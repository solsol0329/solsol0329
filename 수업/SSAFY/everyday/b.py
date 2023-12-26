for t in range(10):
    T=int(input())
    N=int(input())
    arr=[list(str(input())) for _ in range(N)]
    dic={'A': 1, 'B': 2, 'C': 3}
    lst=[]
    count=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count+=1
            if arr[i][j]=='A' or arr[i][j]=='B' or arr[i][j] == 'C':
                lst.append((i,j))

    for i,j in lst:
        for l in range(1, dic[arr[i][j]]+1):
            if arr[i + l][j] =='H':
                count-=1
                arr[i + l][j] ='X'
            if arr[i][j -l] =='H':
                count-=1
                arr[i][j -l] ='X'
            if arr[i -l][j] =='H':
                count-=1
                arr[i -l][j] ='X'
            if arr[i][j + l] =='H':
                count-=1
                arr[i][j + l] ='X'

    print(f'#{T} {count}')
    
    
# for t in range(10):
#     T=int(input())
#     N=int(input())
#     arr=[list(str(input())) for _ in range(N)]
#     ai=[1,0,-1,0]
#     aj=[0,-1,0,1]
#     dic={'A': 1, 'B': 2, 'C': 3}
#     lst=[]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]=='A' and arr[i][j]=='B' and arr[i][j] == 'C':
#                 lst.append((i,j))
# 
#     for k in range(4):
#         for i, j in lst:
#             for l in range(1, dic[arr[i][j]]):
#                 ni = i + ai[k] * l
#                 nj = j + aj[k] * l
#                 arr[ni][nj] = 'X'
# 
#     count=0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'H':
#                 count+=1

    # print(f'#{T} {count}')
    
    
    
    
    
    # ai=[1,0,-1,0]
# aj=[0,-1,0,1]
# for t in range(10):
#     T=int(input())
#     N=int(input())
#     arr=[list(str(input())) for _ in range(N)]
#     lst_a=[]
#     lst_b = []
#     lst_c = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]=='A':
#                 lst_a.append((i,j))
#             elif arr[i][j]=='B':
#                 lst_b.append((i,j))
#             elif arr[i][j] == 'C':
#                 lst_c.append((i, j))
# 
#     for k in range(4):
#         for i,j in lst_a:
#             ni = i + ai[k]
#             nj = j + aj[k]
#             arr[ni][nj] = 'X'
#         for i,j in lst_b:
#             for l in range(1, 3):
#                 ni = i + ai[k] * l
#                 nj = j + aj[k] * l
#                 arr[ni][nj] = 'X'
#         for i,j in lst_c:
#             for l in range(1, 4):
#                 ni = i + ai[k] * l
#                 nj = j + aj[k] * l
#                 arr[ni][nj] = 'X'
# 
#     count=0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'H':
#                 count+=1

    # print(f'#{T} {count}')