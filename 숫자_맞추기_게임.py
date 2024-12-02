import random as r

# 1부터 10까지의 정수를 임의로 선택
random_number = r.randint(1,10)

print('1과 10 사이의 숫자를 하나 정했습니다.')
print("이 숫자는 무엇일까요?")
# 사용자의 숫자를 입력 받아 숫자를 맞추는 반복문
while True:
    user_number = int(input('예상 숫자: '))
    
    # 사용자의 답이 정답과 맞다면 종료
    if user_number == random_number:
        print("정답입니다!")
        break
    
    # 사용자의 답이 정답과 다르다면 다시 반복.
    elif user_number > random_number:
        print("너무 큽니다. 다시 입력하세요.")
    elif user_number < random_number:
        print('너무 작습니다. 다시 입력하세요')
