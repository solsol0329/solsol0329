import sys; sys.stdin = open('최소이동거리_input.txt')

def dijkstra(s):
    # 1. 시작점 설정
    D[s] = 0
    # 2. 정점갯수 만큼 반복
    for _ in range(V):
        # 2-1. 최소값
        min_v = INF
        for i in range(V):
            if not visited[i] and min_v > D[i]:
                min_v = D[i]
                v = i # 시작정점
        # 2-2. 방문체크
        visited[v] = 1
        # 여기서 할일을 체크 해서 정답을 리턴함.
        # if v == N:
        #     return D[v]
        # 2-3. 가중치 갱신
        for w in range(V):
            if adj[v][w] and not visited[w]:
                if D[w] > D[v] + adj[v][w]:
                    D[w] = D[v] + adj[v][w]

INF = 987654321
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    V = N + 1                        # 정점의 갯수 (0 ~ N)
    adj = [[0] * V for _ in range(V)]  # 인접행렬
    D = [INF] * V                      # 가중칠 배열
    visited = [0] * V                  # 방문리스트
    # 인접행렬 만들기
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w   # 방향성 있음
    dijkstra(0)
    print(f'#{tc} {D[N]}')
