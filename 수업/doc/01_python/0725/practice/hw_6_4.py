# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    # new_dict[key] = value
    new_dict.update({key: value})
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
# my_dict['name'] = 'kim'   # 수정
# my_dict['addr'] = 'gumi'  # 추가
# print(my_dict['addr'])
# print(my_dict.get('addr'))55
age = 20
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
