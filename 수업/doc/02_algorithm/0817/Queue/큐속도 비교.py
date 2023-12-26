import time
start = time.time()

SIZE = 1_000_000
# Q = [0] * SIZE
# f = r = -1
# for i in range(SIZE):
#     r += 1
#     Q[r] = i
#
# while f != r:
#     f += 1
#     tmp = Q[f]
from collections import deque
Q = deque()
for i in range(SIZE):
    Q.append(i)
while Q:
    tmp = Q.popleft()

print(time.time() - start)

