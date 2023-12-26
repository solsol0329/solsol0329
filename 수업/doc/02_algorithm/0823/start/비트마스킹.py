visited1 = [1, 0, 0, 0, 1]   # 0, 4번 방문
visited2 = 0b10001
print(visited2)
###############################
visited = 0
# 원소 추가
visited = visited | 1 << 3
print(visited, bin(visited))

# 원소 제거
visited = visited & ~(1 << 3)
print(visited, bin(visited))

# 원소 조회
visited = visited | 1 << 3
print(visited & (1 << 3))
visited = visited & ~(1 << 3)
print(visited & (1 << 3))

# 원소 토글
visited = visited ^ (1<<3)
print(visited, bin(visited))
visited = visited ^ (1<<3)
print(visited, bin(visited))
visited = visited ^ (1<<3)
print(visited, bin(visited))