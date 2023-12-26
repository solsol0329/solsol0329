my_list = [3, 2, 1]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
# ----------------------
my_list2 = [3, 2, 1]
print(sorted(my_list2))
print(my_list2)
# --------------------
my_list3 = [
    ['홍', 35, 'seoul'],
    ['김', 25, 'gumi'],
    ['이', 30, 'daegu']
]
my_list3.sort(key=lambda x: x[1], reverse=True)
print(my_list3)