import sys; sys.stdin = open('반복문자지우기_input.txt')
def is_empty(stack):
    if top == -1:
        return True
    else:
        return False

def push(stack, item):
    global top
    top += 1
    stack[top] = item

def pop(stack):    # 비어있는지 확인하기
    global top
    if top == -1:
        return
    else:
        result = stack[top]
        top -= 1
        return result

def peek(stack):
    return stack[top]

T = int(input())
for tc in range(1, T+1):
    str = input()
    N = len(str)
    stack = [0] * 1000
    top = -1

    for i in range(N):
        if is_empty(stack):     # 스택이 비어 있으면 -> push()
            push(stack, str[i])
        else:                   # 스택이 비어 있지 않으면
            # 스택의 맨위 원소와 비교
            if peek(stack) == str[i]:
                pop(stack)
            else:
                push(stack, str[i])

    print(f'#{tc} {top+1}')
