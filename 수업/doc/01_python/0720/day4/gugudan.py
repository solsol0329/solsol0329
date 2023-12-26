# for i in range(2, 10): 
#     print(f'{i}단')
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')
#     print('-----------')

i = 2
while i < 10:
    j = 1
    while j < 10:
        print(f'{i} * {j} = {i*j}')
        j += 1
    i += 1