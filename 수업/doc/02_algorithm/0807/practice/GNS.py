import sys;
sys.stdin = open('GNS_input.txt', 'r')
sys.stdout = open('GNS_output.txt', 'w')

digits = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    no, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))

    # 카운팅
    counts = [0] * 10
    for i in range(N):
        for j in range(10):
            if arr[i] == digits[j]:
                counts[j] += 1
    # 출력
    print(f'#{tc}')
    for i in range(10):
        for j in range(counts[i]):
            print(digits[i], end=' ')
    print()

