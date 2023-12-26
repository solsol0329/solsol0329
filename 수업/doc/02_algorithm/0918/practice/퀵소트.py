import sys; sys.stdin = open('퀵소트_input.txt')
def hoare_partition(a, l, r):
    a[l], a[r] = a[r], a[l]  # 오른쪽 걸로 선택시
    pivot = a[l]
    i, j = l, r

    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] >= pivot:
            j -= 1
        if i < j :
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quicksort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)

        quicksort(a, l, pivot-1)
        quicksort(a, pivot+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')