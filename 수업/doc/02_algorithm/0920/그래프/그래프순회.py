'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in adj_list[v]:  # 인접한
        if visited[w] == 0:
            dfs(w)

def bfs(v):
    Q = [v]  # 만들고 인큐
    visited[v] = 1
    while Q:
        v = Q.pop(0) # 디큐
        # 하고싶은일 하기
        print(v)
        for w in adj_list[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]    # 인접리스트 초기화
visited = [0] * (V+1)

# 인접리스트 만들기
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)
print(adj_list)
# dfs(1)
bfs(1)
print(visited)