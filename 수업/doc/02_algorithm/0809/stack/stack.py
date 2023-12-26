def push(item):
    global top
    if top > SIZE -1 :
        return
    else:
        top += 1   # top 증가시키고 넣기
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('Stack is empty!')
        return
    else:
        result = stack[top]
        top -= 1
        return result

SIZE = 100
stack = [0] * SIZE
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())
print(stack)