def union_sets(set1, set2):
    return set1 | set2

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)

def union_sets2(set1, set2):
    return set1.union(set2)

result = union_sets2({1, 2, 3}, {3, 4, 5})
print(result)