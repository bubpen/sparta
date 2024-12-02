class person():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def display(self):
        print(f"이름 : {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")
        
        
name = input("이름: ")
gender = input('성별(male or female): ')
age = int(input("나이: "))
name = person(name,gender,age)
name.display()