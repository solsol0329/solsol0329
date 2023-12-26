'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:  # 인접한 정점중에 미방문 정점(w)
            dfs(w)


V, E = map(int, input().split())        # 정점, 간선
temp = list(map(int, input().split()))
adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 초기화
visited = [0] * (V+1)                   # 방문기록

for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    adj[s][e] = adj[e][s] = 1

dfs(1)