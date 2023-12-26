import time
start_time = time.time()

import sys
sys.stdin = open("최대상금_input.txt", "r")

def dfs(n, k, prize):
    global ans
    money = int("".join(prize))

    if (money, k) in visited:  # 메모이제이션
        return

    visited.append((money, k)) # visited에 추가

    if k == n:
        ans = max(ans, int(money))
        return

    for i in range(len(prize)-1):
        for j in range(i + 1, len(prize)):
            prize[i], prize[j] = prize[j], prize[i]
            dfs(n, k + 1, prize)
            prize[i], prize[j] = prize[j], prize[i]


for tc in range(1, int(input()) + 1):
    prize, N = map(str, input().split())
    prize = list(prize)
    visited = []   # 금액과 k
    N = int(N)

    ans = 0
    dfs(N, 0, prize)
    print("#{} {}".format(tc, ans))

print(time.time() - start_time, 'seconds')