def itoa(num):   # 123
    arr = []
    while num:
        value = num % 10  #  1
        num //= 10 # 0
        arr.append(value) # |3|2|1|
    arr.reverse()
    return arr

def atoi(arr): # |3|2|1|
    value = 0
    for i in range(len(arr)):
        value = value * 10 + arr[i]
    return value


num = 123
arr = itoa(num)
print(arr)
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)
num = atoi(arr)
print(num)
