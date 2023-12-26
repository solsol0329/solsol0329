import sys; sys.stdin = open('최소신장트리_input.txt')
def find_set(x):
    if P[x] == x:
        return x
    else:
        return find_set(P[x])

def kruskal():
    # 0. 초기화
    total = 0
    cnt = 0   # 간선의 갯수
    # 1. 간선의 배열 가중치 정렬
    edges.sort(key=lambda x:(x[2], x[0]))
    # 2. 간선을 V개 선택 해야 한다.(정점이 0~V번 )
    for i in range(E):
        # 2-1.각정점의 find-set 비교
        p1 = find_set(edges[i][0])
        p2 = find_set(edges[i][1])
        if p1 != p2:   # MST 포함
            # 2-1-1. union 및 할일 하기
            P[p2] = p1    # union
            total += edges[i][2]   # 가중치
            cnt += 1
        if cnt == V:
            return total


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    P = list(range(V+1))   # make-set
    print(f'#{tc} {kruskal()}')