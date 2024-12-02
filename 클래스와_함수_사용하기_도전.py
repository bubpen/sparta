# 클래스 정의
class person:
    # 생성자 정의
    def __init__(self, name, gender, age):
        self.name = name
        # 성별을 male 혹은 female 이어야만 저장되게 반복.
        while True:
            if gender == 'male' or gender == 'female':
                self.gender = gender
                break
            else:
                gender = input("성별이 잘못 입력되었습니다. 'male' 혹은 'female'을 입력해주세요. \n 성별: ").lower()
        self.age = age
        
    def display(self):
        print(f"이름 : {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")
    
    # 나이 별로 인사를 정의
    def greet(self):
        if self.age <= 13:
            print(f'안녕하세요, {self.name}! 어린이 분이시네요!')
        elif self.age <20:
            print(f'안녕하세요, {self.name}! 청소년이시군요!')
        else:
            print(f'안녕하세요, {self.name}! 성인이시군요!')
        
# 정보 입력         
age = int(input("나이: "))
name = input("이름: ")
gender = input('성별(male or female): ')


# 객체 생성
name = person(name,gender,age)

# 클래스 메서드 호출
name.display()

name.greet()