def fact(n):
    # 기본파트 : 멈추는 부분
    if n == 1:
        return 1
    # 유도파트 : 재귀호출
    else:
        return n * fact(n-1)

print(fact(4))