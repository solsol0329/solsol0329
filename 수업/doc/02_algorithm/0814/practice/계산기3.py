import sys; sys.stdin=open('계산기3_input.txt')
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
def infix_to_postfix(exp):
    stack = []
    result = []
    for tok in exp:
        # 피연산자
        if '0' <= tok <= '9':
            result.append(tok)
        # ')'
        elif tok == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop() # 왼쪽괄호 제거
        # 연산자 + '('
        else:
            if stack:
                while icp[tok] <= isp[stack[-1]]:
                    result.append(stack.pop())
                    if not stack: break
            stack.append(tok)

    while stack:
        result.append(stack.pop())

    return ''.join(result)

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = infix_to_postfix(infix)
    print(postfix)