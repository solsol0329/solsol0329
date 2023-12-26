def intersection_sets(set1, set2):
    return set1 & set2

def intersection_sets2(set1, set2):
    return set1.intersection(set2)

result = intersection_sets({1, 2, 3}, {3, 4, 5})
result = intersection_sets2({1, 2, 3}, {3, 4, 5})
print(result) # {3}