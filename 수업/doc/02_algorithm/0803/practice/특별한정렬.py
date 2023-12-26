import sys; sys.stdin = open('특별한정렬_input.txt')
def selection(a, n):
    for i in range(10):
        m_idx = i
        if i % 2 :  #홀수 : 최소값
            for j in range(i+1, n):
                if a[m_idx] > a[j]:
                    m_idx = j
        else: # 짝수 : 최대값
            for j in range(i+1, n):
                if a[m_idx] < a[j]:
                    m_idx = j
        a[m_idx], a[i] = a[i], a[m_idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection(arr, N)
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()