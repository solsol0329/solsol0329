# 부분집합의 합이 10인 부분집합 찾기
def powerset(n, k, cursum):    # n: 원소의 갯수, k: 재귀의 깊이
    global count, total
    total += 1
    if cursum > 10 :
        return
    #####################
    if n == k:
        # 합이 10일때 출력
        if cursum == 10:
            count += 1
            for i in range(n):
                if bit[i] :
                    print(arr[i], end=' ')
            print()

    else:
        bit[k] = 1
        powerset(n, k+1, cursum + arr[k])
        bit[k] = 0
        powerset(n, k+1, cursum)


arr =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
bit = [0] * N   # 원소의 포함 여부(0, 1)
count = 0
total = 0
powerset(N, 0, 0)
print(f'count={count}, 호출횟수={total}')