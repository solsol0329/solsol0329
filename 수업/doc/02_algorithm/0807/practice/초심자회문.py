import sys; sys.stdin = open('초심자회문_input.txt')
T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    flag = 1
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            flag = 0
            break
    print(f'#{tc} {flag}')