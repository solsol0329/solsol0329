import sys; sys.stdin = open('그룹나누기_input.txt')

def bfs(v):
    # 인큐 + 방문체크
    Q = [v]
    visited[v] = 1
    # while
    while Q:
        # 디큐 + 하고싶은일
        v = Q.pop(0)
        # 인접하고 미방문
        for w in adj[v]:
            if not visited[w]:
            # 인큐 + 방문체크
                Q.append(w)
                visited[w] = 1

def dfs(v):
    # 방문체크
    visited[v] = 1
    # 인접하고 미방문
    for w in adj[v]:
        if visited[w] == 0:
        # 재귀
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  #정점, 간선
    tmp = list(map(int, input().split()))
    adj = [[] for _ in range(V+1)]  # 인접리스트
    visited = [0] * (V+1)

    # 인접리스트 채우기
    for i in range(E):
        s, e  = tmp[2*i], tmp[2*i+1]
        adj[s].append(e)
        adj[e].append(s)

    cnt = 0
    for i in range(1, V+1):
        if not visited[i]:
            # bfs(i)
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')


