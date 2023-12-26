import sys; sys.stdin = open('이진힙_input.txt')
def enQ(v):
    global last
    # (1) 완전이진트리
    last += 1
    heap[last] = v
    # (2) 부모 < 자식  (최소힙)
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def find_a():
    p = last // 2
    sum_v = 0
    while p:
        sum_v += heap[p]
        p //= 2
    return sum_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    last = 0
    heap = [0] * (N+1)
    tmp = list(map(int, input().split()))
    for i in range(N):
        enQ(tmp[i])
    print(f'#{tc} {find_a()}')