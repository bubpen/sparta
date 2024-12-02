# 클래스 정의
class person:
    # 생성자 정의
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    # 이름, 성별, 나이를 출력하는 메서드를 정의
    def display(self):
        print(f"이름 : {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")
        
# 이름, 성별, 나이 입력
name = input("이름: ")
gender = input('성별(male or female): ')
age = int(input("나이: "))

# 객체 생성
name = person(name,gender,age)

# 클래스 메서드 호출
name.display()
