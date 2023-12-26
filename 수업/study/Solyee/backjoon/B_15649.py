def per(n,arr):
    if n==M:
        print(*arr)
        return
    else:
        for i in range(N):
            if visited[i]==0:
                visited[i]=1
                per(n+1,arr+[num_lst[i]])
                visited[i]=0


N,M=map(int,input().split())
num_lst=list(range(1,N+1))
visited=[0]*N
per(0,[])
