import random as r
while True:
    # 1부터 10 사이의 숫자를 랜덤으로 설정
    random_number = r.randint(1,10) 
    print('1과 10 사이의 숫자를 하나 정했습니다.')
    print("이 숫자는 무엇일까요?")
    while True:
        # 입력받은 수를 문자형 데이터에서 정수형 데이터로 변환
        user_number = int(input('예상 숫자: ')) 
        # 수의 범위에서 벗어난 경우
        if user_number < 1 or user_number > 10:
            print("1부터 10사이의 숫자로 다시 입력해주세요.")
        # 정답일 경우, 내부 반복문 종료
        elif user_number == random_number:
            print("정답입니다!")
            break
        # 답이 아닐 경우
        elif user_number > random_number:
            print("너무 큽니다. 다시 입력하세요.")
        elif user_number < random_number:
            print('너무 작습니다. 다시 입력하세요')
    # 내부 반복문 종료 후 진행
    # 다시 진행할 것인지 사용자의 대답을 입력
    user_option = input('게임을 다시 하시겠습니까? (y/n): ').lower()
    # 대답이 'n'혹은 'N'이라면 정상 종료
    if user_option == 'n':
        print("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
        break # 외부 반복문 종료
