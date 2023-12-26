class Person:
    # 클래스 변수
    count = 0
    # 생성자
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        Person.count += 1
    
    def talk(self): # 인스턴스 메소드
        print(f'안녕 {self.name}입니다.')

    @classmethod
    def num_of_pop(cls):
        print(f'인구수 : {cls.count}')

    @staticmethod
    def greeting():
        print('hello')

    def __str__(self):
        return f'{self.name}입니다.'

p1 = Person('iu')
p1.talk()
p2 = Person('BTS')
p2.talk()
Person.num_of_pop()
Person.greeting()
print(p1)