import sys;
sys.stdin=open('버스노선_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001

    # 카운팅
    for i in range(N):
        S, E = map(int, input().split())
        for j in range(S, E + 1):
            counts[j] += 1
    # 각 정류장에 몇개의 버스 노선이 운행
    P = int(input())
    ans = []
    for _ in range(P):
        p = int(input())
        ans.append(counts[p])

    print(f'#{tc}', *ans)

