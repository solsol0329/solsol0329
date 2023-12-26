my_list = [1, 2, 2, 2, 3, 3]
idx = my_list.count(2)
print(idx)
# --------------------
def my_count(item):
    count = 0
    for num in my_list:
        if num == item:
            count += 1
    return count
print(my_count(3))