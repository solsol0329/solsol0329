# hw_7_4.py

# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0  # 클래스 변수
    
    def __init__(self, n, a): # 생성자 메소드
      self.name = n     # 인스턴스 변수
      self.age = a
      Person.number_of_people += 1
    
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age}입니다.')
    


person1 = Person("Alice", 25)
person2 = Person("kim", 25)
person1.introduce()
print(Person.number_of_people)