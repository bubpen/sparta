import random as r
# 1부터 10 사이의 정수로 정답 설정
random_number = r.randint(1,10)
print('1과 10 사이의 숫자를 하나 정했습니다.')
print("이 숫자는 무엇일까요?")
# 숫자 맞추는 반복문 실행
while True:
    # 사용자의 답을 입력
    user_number = int(input('예상 숫자: '))
    # 정답일 경우, 반복문 종료
    if user_number ==random_number:
        print("정답입니다!")
        break
    # 정답이 아닐 경우
    elif user_number > random_number:
        print("너무 큽니다. 다시 입력하세요.")
    elif user_number < random_number:
        print('너무 작습니다. 다시 입력하세요')
