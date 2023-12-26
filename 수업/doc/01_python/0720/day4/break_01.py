numbers = [1, 3, 5, 5, 7, 9, 13, 11]
is_even = False
for num in numbers: # 1 3 5 5
    # 짝수를 만나면
    if num % 2 == 0:
        print('짝수', num)
        is_even = True
        break
if not is_even:
    print('짝수 없다.')
