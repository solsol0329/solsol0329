import sys; sys.stdin = open('그룹나누기_input.txt')
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  #정점, 간선
    tmp = list(map(int, input().split()))
    parent = list(range(N + 1))   # make-set

    for i in range(M):
        s, e = tmp[2*i], tmp[2*i+1]
        # union
        parent[find_set(e)] = find_set(s)

    cnt = 0
    for i in range(1, N+1):
       if parent[i] == i:
           cnt += 1

    print(f'#{tc} {cnt}')


