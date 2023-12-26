import sys
sys.stdin = open("그래프경로_input.txt")

def solve(s):
    stack = []
    stack.append(s)  #push

    while len(stack) != 0:
        v = stack.pop()
        if v == e: #도착점 찾음
            return 1
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if adj[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())  # 정점, 간선
    # 인접행렬, 1 ~ V
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)             # 방문처리
    for _ in range(E):
        u, v = map(int, input().split()) #시작노드, 끝노드
        adj[u][v] = 1       #인접행렬

    s, e = map(int, input().split())  # 출발노드, 도착노드

    print("#{} {}".format(t, solve(s)))