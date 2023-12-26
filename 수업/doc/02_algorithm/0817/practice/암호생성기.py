import sys
sys.stdin = open('암호생성기_input.txt')

T = 10
for tc in range(1, T+1):
    no = input()
    Q = list(map(int, input().split()))

    cnt = 0
    while True:
        tmp = Q.pop(0)
        tmp -= cnt % 5 + 1
        if tmp < 0: tmp = 0

        Q.append(tmp)
        cnt += 1
        if tmp == 0: break

    print(f'#{tc}', *Q)