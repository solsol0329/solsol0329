# a = 5
# b = a
# b = 50
# print(a, b)

# 0. 할당(assignment)
# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(a, b)

# 2. 얕은 복사(shallow copy)
# 1차원배열
# a = [1, 2, 3]
# b = a[:]
# print(id(a), id(b))
# print(a == b)
# print(a is b)
# b[0] = 5
# print(a, b)

# 2차원 배열
# import copy
# a =[
#     [1, 2], 
#     [3, 4]
# ]

# # b = a[:]
# # b = list(a)
# b = copy.copy(a)

# # print(id(a), id(b))
# # print(id(a[0]), id(b[0]))
# a[0] = [8, 9]
# a[1][0] = 100
# a[1].append(500)
# print(a, b)

# 2. 깊은 복사(deepcopy)
import copy
a =[
    [1, 2], 
    [3, 4]
]
b = copy.deepcopy(a)
a[1].append(5)
print(a, b)
