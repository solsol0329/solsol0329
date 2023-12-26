############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    result  = 0
    for num in range(2, number):
        is_prime = True
        if num == 17: continue
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result += num
    return result

# 아래 코드는 실행을 위한 코드입니다. 
if __name__ == '__main__':
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.