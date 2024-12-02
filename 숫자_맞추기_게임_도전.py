import random as r
# 숫자 맞추기 전체 반복문
while True:
    
    # 1부터 10 사이의 숫자를 랜덤으로 설정
    random_number = r.randint(1,10) 
    print('1과 10 사이의 숫자를 하나 정했습니다.')
    print("이 숫자는 무엇일까요?")
    
    # 기본 숫자 맞추는 반복문
    while True:
        user_number = int(input('예상 숫자: ')) # 입력받은 수를 문자형 데이터에서 정수형 데이터로 변환
        
        # 사용자의 답이 수의 범위에서 벗어난 경우
        if user_number < 1 or user_number > 10:
            print("1부터 10사이의 숫자로 다시 입력해주세요.")
        # 사용자의 답이 정답일 경우 내부 반복문을 종료
        elif user_number == random_number: 
            print("정답입니다!")
            break
        
        # 사용자의 답이 정답과 다를 경우
        elif user_number > random_number: 
            print("너무 큽니다. 다시 입력하세요.")
        elif user_number < random_number:
            print('너무 작습니다. 다시 입력하세요')
    
    # 내부 반복문 종료 후 진행. 재반복 여부 확인
    user_option = input('게임을 다시 하시겠습니까? (y/n): ').lower() 
    # 'n'이라면 정상 종료
    if user_option == 'n': 
        print("게임을 종료합니다. 즐거우셨나요? 또 만나요!") 
        break # 외부 반복문 종료
    
    # 입력이 올바르지 않을 경우, 종료
    if user_option != 'y': 
        print('입력이 올바르지 않아 종료합니다.')
        break 
