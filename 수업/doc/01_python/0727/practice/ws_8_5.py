class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    sound = '멍멍'

class Cat(Animal):
    sound = '야옹'

class Pet(Dog, Cat):
    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound}소리를 냅니다.'

pet = Pet()
print(pet)
