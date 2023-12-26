from collections import deque

Q = deque()

# enQ
Q.append(1)
Q.append(2)
Q.append(3)
# peek
print(f'peek : {Q[0]}')
# deQ
while Q:
    print(Q.popleft())
