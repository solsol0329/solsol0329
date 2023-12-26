N = 20                  # 마이쮸 갯수
q = [(1, 1)]             # (사람번호, 직전까지 받았던 마이쥬의 개수)
                        # 1번이 줄을 서고 아직 받지 않은 상태

new_people = 1          # 새롭게 줄을 서는 사람 번호
last_people = 0         # 마지막으로 받아간 사람
print(N, q)
while N > 0:                    # 마이쮸가 남아있는 동안
    num, cnt = q.pop(0)         # 줄의 맨 앞사람, num번, cnt 이전에 받은 개수
    N -= cnt  # 남은 마이쥬 개수
    last_people = num
    new_people += 1             # 새로 줄서는 사람의 번호
    input()
    print(num, cnt, N, end=' ')

    cnt += 1                    # 이번에 받을 개수
    q.append((num, cnt))        # 맨 앞사람이 cnt개를 받아서 줄을 섬
    q.append((new_people, 1))   # 새로 줄서는 사람, 아직 0개
    print(q)

print(last_people)
