arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n): # 0 ~ 2^n 되기 전까지
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()
print()