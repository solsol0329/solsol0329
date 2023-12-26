def binary_search(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        # 1. mid값 = key
        if a[mid] == key:
            return (True, mid)
        # 2. mid값 > key
        elif a[mid] > key:
            end = mid - 1
        # 3. mid값 < key
        else:
            start = mid + 1
    return (False, -1)


key = 12
arr = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(arr, len(arr), key))