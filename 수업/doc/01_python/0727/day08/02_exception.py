try:
    num = int(input())
    result = 10 / num
except ZeroDivisionError:
    print('0으로 나눌수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요')
except BaseException:
    print('입력을 확인하세요.')
except:
    print('에러가 발생하였습니다.')