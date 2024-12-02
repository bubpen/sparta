import random as r
while True:
    a = r.randint(1,10) # 1부터 10 사이의 숫자를 랜덤으로 설정
    print('1과 10 사이의 숫자를 하나 정했습니다.')
    print("이 숫자는 무엇일까요?")
    while True:
        n = int(input('예상 숫자: ')) # 입력받은 수를 문자형 데이터에서 정수형 데이터로 변환
        if n < 1 or n > 10: # 수의 범위에서 벗어난 경우
            print("1부터 10사이의 숫자로 다시 입력해주세요.")
        elif n ==a: # 정답일 경우
            print("정답입니다!")
            break # 내부 반복문 종료
        elif n > a: # 클 경우
            print("너무 큽니다. 다시 입력하세요.")
        elif n < a: # 작을 경우
            print('너무 작습니다. 다시 입력하세요')
    y = input('게임을 다시 하시겠습니까? (y/n): ').lower() # 내부 반복문 종료 후 진행
    if y == 'n':
        print("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
        break # 외부 반복문 종료