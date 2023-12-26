# Queue는 초기 크기를 크게 잡아야 한다.
SIZE = 100
Q = [0] * SIZE
front = rear = -1

#enQueue
rear += 1
Q[rear] = 1
rear += 1
Q[rear] = 2
rear += 1
Q[rear] = 3

# peek
print(f'peek : {Q[front+1]}')

# deQueue
while front != rear:
    front += 1
    print(Q[front])

print(front, rear)
print(Q)








