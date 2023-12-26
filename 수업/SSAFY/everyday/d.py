
def prim(s):
    total = 0
    D[s] = 0


    for _ in range(V+1):
        min_n = 987654321
        for i in range(V+1):
            if visited[i] == 0 and D[i] < min_n:
                min_n = D[i]
                v = i
        visited[v] = 1
        total += D[v]
        for j in range(V+1):
            if adj[v][j]!=0 and not visited[j]:
                if D[j] > adj[v][j]:
                    D[j] = adj[v][j]
                    parent[j] = v
    return total


T= int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    parent = list(range(V+1))
    D = [987654321] * (V+1)
    for _ in range(E):
        s, e, w = map(int,input().split())
        adj[s][e] = adj[e][s] = w
    print(f'#{t} {prim(0)}')