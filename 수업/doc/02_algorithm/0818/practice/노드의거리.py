import sys; sys.stdin = open('노드의거리_input.txt')
def bfs(v):
    Q = [v] # 인큐 + 방문체크
    visited[v] = 1

    while Q:
        # deQ + 하고싶은일
        v = Q.pop(0)
        if v == G: return visited[v] - 1

        for w in range(1, V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1
    S, G = map(int, input().split())
    # bfs(S)
    # if visited[G] :
    #     print(f'#{tc} {visited[G]-1}')
    # else:
    #     print(f'#{tc} {0}')
    print(f'#{tc} {bfs(S)}')