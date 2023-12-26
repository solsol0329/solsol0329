# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(t):
  new_tuple = ()
  sorted_list = sorted(t)
  for item in sorted_list:
    new_tuple += (item, )
  return new_tuple

def sort_tuple2(t):
  return tuple(sorted(t))

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
result = sort_tuple2((5, 2, 8, 1, 3))
print(result)
