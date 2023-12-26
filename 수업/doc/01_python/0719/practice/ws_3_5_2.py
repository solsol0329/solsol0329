from book import decrease_book
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_info ={
        'name': name, 
        'age': age,
        'address': address,
    }
    print(f'{name}님 환영합니다.')
    return user_info

def rental_book(info):
    decrease_book(info['age'])
    print(f"{info['name']}님이 {info['age']}권의 책을 대여하였습니다.")

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_info = []

for n, a, ad in zip(name, age, address):
    increase_user()
    user_info.append({
        'name': n,
        'age': a ,
        'address':ad,
    })
    print(f'{n}님 환영합니다.')

# print(user_info)
for info in user_info:
    rental_book({
        'name': info['name'],
        'age': info['age'] // 10,
    })

