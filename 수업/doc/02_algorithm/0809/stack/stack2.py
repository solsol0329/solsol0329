stack = [0] * 100
top = -1

top += 1
stack[top] = 1
top += 1
stack[top] = 2
top += 1
stack[top] = 3

while top != -1:
    print(stack[top])
    top -= 1
