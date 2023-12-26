N=int(input())
for i in range(1,N+1):
    a= i % 10  # 일의 자리 수
    bb= i // 10 # i가 10의 자리 수 일 때 십의 자리 수
    bbb= (i % 100) - (i % 10) # i가 100의 자리 수 일 때 십의 자리 수
    ccc = i // 100


    if i < 10:  # i가 일의 자리수 일 때
        if i % 3 != 0:  # i를 3으로 나눈 몫이 0이 아닐 때 => i가 3의 배수가 아닐 때 i를 프린트 해라
            print(i) 
        else:
            print('_')  # 그 외의 경우 => i가 3의 배수일 때 _ 를 프린트 해라
    elif i < 100:   #  i가 십의 자리수 일 때
        if bb % 3 == 0 and (a != 0 and a % 3 == 0):  #  i의 십의 자리수와 일의 자리수 모두 3의 배수일 때 __를 프린트 해라
            print('__')
        elif bb % 3 != 0 and (a == 0 or a % 3 != 0):  # i의 십의 자리수와 일의 자리수가 모두 3의 배수가 아닐 때 i를 출력 
            print(i)
        else:   # 그 외의 경우 => i의 십의 자리수와 일의 자리수 중 하나가 3의 배수일 때 _ 출력하기
            print('_')


    else:  # i가 백의 자리수 일 때
        if ccc % 3 == 0 and (bbb % 3 == 0 and bbb != 0) and (a % 3 == 0 and a != 0 ):  #  i의 백의 자리수와 십의 자리수, 일의 자리 수 모도 3의 배수일 때
            print('___')
        elif ccc % 3 != 0 and (bbb % 3 != 0 or bbb == 0) and (a == 0 or a % 3 != 0): # 모든 자리수가 3의 배수가 아닐 때
            print(i)
        elif ccc % 3 == 0 or (bbb % 3 == 0 and bbb != 0) or (a % 3 == 0 and a != 0 ): # 백, 십, 일의 자리 수 중 하나만 3의 배수일 때
            print('_')
        else:
            print('__')

            