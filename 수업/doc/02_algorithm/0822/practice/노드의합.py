import sys; sys.stdin = open('노드의합_input.txt')
def post(v):
    if v <= N:
        post(v * 2)
        post(v * 2 + 1)
        # 왼쪽 + 오른쪽
        if v*2+1 <= N:
            tree[v] = tree[v*2] + tree[v*2+1]
        elif v*2 <= N:
            tree[v] = tree[v*2]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num
    post(L)
    print(f'#{tc} {tree[L]}')