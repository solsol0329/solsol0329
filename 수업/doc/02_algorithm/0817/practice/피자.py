import sys;sys.stdin = open('피자_input.txt')
def solve():
    Q = []
    # 화덕에 피자 넣기
    for i in range(1, N+1):
        Q.append(i)
    idx = N + 1  # 다음에 화덕에 들어갈 피자번호
    while len(Q) > 1:
        # 피자를 꺼내서 치즈 확인
        pizza = Q.pop(0)
        cheese[pizza] //= 2
        # 치즈가 남아 있으면
        if cheese[pizza] > 0:
            Q.append(pizza)
        # 치즈가 다 녹았으면, 다음피자 넣기
        elif idx <= M:
            Q.append(idx)
            idx += 1
    return Q[0]

T = int(input())
for tc in range(1, T+1):
    # 화덕크기, 피자수
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))
    print(f'#{tc} {solve()}')