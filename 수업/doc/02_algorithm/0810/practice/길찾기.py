import sys
sys.stdin = open("길찾기_input.txt")

def dfs(v):
    global flag
    # 방문처리
    visited[v] = 1
    # 도착점인지 확인
    if v == GOAL:
        flag = 1
        return

    # 시작정점(v)에 인접정점(w)중에 방문 안한 정점 재귀로 호출
    for w in range(0, SIZE):
        if adj[v][w] == 1 and visited[w] ==0:
            dfs(w)

T = 10
SIZE = 100
START = 0
GOAL = 99

for tc in range(1, T + 1):
    flag = 0  # 정답
    no, E = map(int, input().split())
    temp = list(map(int, input().split()))
    # 인접행렬  100 X 100
    adj = [[0] * SIZE for _ in range(SIZE)]
    visited = [0] * SIZE
    for i in range(E):
        s, e = temp[2 * i], temp[2 * i + 1]
        adj[s][e] = 1  # 방향성 있음

    dfs(START)
    print("#{} {}".format(tc, visited[GOAL]))
    print("#{} {}".format(tc, flag))

