# words = ['hello', 'world']
# text = '-'.join(words)
# print(text)

text = 'Komputer'
print(text, type(text))
# str -> list
lst = list(text)
print(lst, type(lst))
lst[0] = 'C'
print(lst, type(lst))
# list -> str
text = ''.join(lst)
print(text, type(text))

lst2 = [1, 2, 3, 4]
print(''.join(map(str, lst2)))
