def get_keys_from_dict(dictionary):
    return list(dictionary.keys())


def get_keys_from_dict(dictionary):
    keys = []
    for key in dictionary:
        keys.append(key)
    return keys

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)