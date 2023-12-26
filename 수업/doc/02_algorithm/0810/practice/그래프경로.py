import sys; sys.stdin = open('그래프경로_input.txt')
def dfs(v):
    global flag
    visited[v] = 1  # 방문체크
    if v == G:
        flag = 1
        return

    # 인접하고 미방문 정점(w)
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
        # 재귀호출(w)
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        s, e = map(int, input().split())  # 간선입력
        adj[s][e] = 1  # 유향그래프
    S, G = map(int, input().split())

    flag = 0
    dfs(S)
    # print(f'#{tc} {visited[G]}')
    print(f'#{tc} {flag}')