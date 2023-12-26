import sys;
sys.stdin = open('String_input.txt', encoding='UTF-8')
def my_find(t, p):
    global ans
    for i in range(len(t)-len(p)+1): # text
        flag = 1
        for j in range(len(p)): # pattern
            if t[i+j] != p[j]:
                flag = 0
                break
        if flag:
            ans += 1


T = 10
for tc in range(1, T+1):
    no = int(input())
    pattern = input()
    text = input()
    ans = 0
    my_find(text, pattern)
    print(f'#{tc} {ans}')