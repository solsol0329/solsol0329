class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):  # 상속받음
    # def __init__(self, name, age, number, email, student_id):
    #     super().__init__(name, age, number, email)
    #     self.student_id = student_id
    pass

s1 = Student('kim', 25, 1, 'kim@ssafy.com')
