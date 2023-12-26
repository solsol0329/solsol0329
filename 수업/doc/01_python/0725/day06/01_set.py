my_set ={1, 2, 3, 40, 500, 6, 7, 'abc', 'kim'}
my_set.add(1)
print(my_set)
# my_set.remove(30)
my_set.discard(30)

for _ in range(len(my_set)):
    print(my_set.pop())