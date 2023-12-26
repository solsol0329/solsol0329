import sys; sys.stdin = open('이진수1_input.txt')
hex_bin = [
    [0, 0, 0, 0],   # 0
    [0, 0, 0, 1],   # 1
    [0, 0, 1, 0],   # 2
    [0, 0, 1, 1],   # 3
    [0, 1, 0, 0],   # 4
    [0, 1, 0, 1],   # 5
    [0, 1, 1, 0],   # 6
    [0, 1, 1, 1],   # 7
    [1, 0, 0, 0],   # 8
    [1, 0, 0, 1],   # 9
    [1, 0, 1, 0],   # 10
    [1, 0, 1, 1],   # 11
    [1, 1, 0, 0],   # 12
    [1, 1, 0, 1],   # 13
    [1, 1, 1, 0],   # 14
    [1, 1, 1, 1]    # 15
]

def a_to_dec(c):  # 16진수 -> 10진수로...
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def make_bin(x):  # 10진수 -> 2진수
    for i in range(4):
        ans.append(hex_bin[x][i])

T = int(input())
for tc in range(1, T+1):
    n, hex = input().split()
    ans = []
    for i in range(len(hex)):
        make_bin(a_to_dec(hex[i]))
    print(f"#{tc} {''.join(map(str, ans))}")