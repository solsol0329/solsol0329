def selection_sort(a, n):
    for i in range(n-1):
        # 최소값구하기
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


arr = [64, 25, 10, 22, 11]
N = len(arr)
selection_sort(arr, N)
print(arr)