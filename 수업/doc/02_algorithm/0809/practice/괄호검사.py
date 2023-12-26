import sys; sys.stdin = open('괄호검사_input.txt')
def solve(str):
    stack = []

    # 문자열을 스캔
    for i in range(len(str)):
        if str[i] == '(' or str[i] =='{':  # 왼쪽 괄호 일 때
            stack.append(str[i])
        elif str[i] in [')', '}']:         # 오른쪽 괄호 일 때
            if not stack:                    # is_empty : len(stack) == 0
                return 0
            else:
                temp = stack.pop()

                # 같은종류인지 검사
                if str[i] == ')' and temp != '(':
                    return 0
                elif str[i] == '}' and temp != '{':
                    return 0

    if stack: return 0  # 왼쪽남을때  len(stack) != 0

    return 1   # 앞에서 다 통과하면 1을 리턴


T = int(input())
for tc in range(1, T+1):
    str = input()
    print(f'#{tc} {solve(str)}')