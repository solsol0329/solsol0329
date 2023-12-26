import sys; sys.stdin = open('글자수_input.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    my_dict = {}
    # 중복제거 및 0으로 초기화
    for key in str1:
        my_dict[key] = 0
    # 카운팅
    for key in str2:
        if key in my_dict:
        #if my_dict.get(key) != None:
            my_dict[key] += 1
    # 최대값
    ans = 0
    for c in my_dict.values():
        if ans < c: ans = c
    print(f'#{tc} {ans}')