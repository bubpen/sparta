# 클래스 정의
class person():
    # 생성자 정의
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    # 메서드 정의
    def display(self):
        print(f"이름 : {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")
        
# 정보 기입
age = int(input("나이: "))
name = input("이름: ")
gender = input('성별(male or female): ')

#객체 생성
faker = person(name,gender,age)

# 메서드 생성
faker.display()
