############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    result = ''
    for ch in word:
        if ch.isupper():
           ch = chr( 65 + (ord(ch) - 65 + num) % 26)
        elif ch.islower():
           ch = chr(97 + (ord(ch) - 97 + num ) % 26)
        result += ch
    return result


# 아래 코드는 실행을 위한 코드입니다. 
if __name__ == '__main__':
    # 아래의 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.