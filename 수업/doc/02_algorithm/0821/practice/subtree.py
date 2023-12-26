import sys; sys.stdin = open('subtree_input.txt')
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    tmp = list(map(int, input().split()))
    for i in range(E):
        p = tmp[i*2]
        c = tmp[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')