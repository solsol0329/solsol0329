import sys; sys.stdin = open('Forth_input.txt')
def forth(arr):
    stack = []
    for tok in arr:
        # 피연산자
        if tok.isdigit():
            stack.append(tok)
        # 연산자
        elif tok == '+' or tok == '-' or tok == '*' or tok=='/':
            if len(stack) >= 2:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if tok == '+':
                    stack.append(op1 + op2)
                elif tok == '-':
                    stack.append(op1 - op2)
                elif tok == '*':
                    stack.append(op1 * op2)
                elif tok == '/':
                    stack.append(op1 // op2)
            else:
                return 'error'
        # 점
        elif tok == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    print(f'#{tc} {forth(arr)}')