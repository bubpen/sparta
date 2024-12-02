import random as r
a = r.randint(1,10)
print('1과 10 사이의 숫자를 하나 정했습니다.')
print("이 숫자는 무엇일까요?")
while True:
    n = int(input('예상 숫자: '))
    if n ==a:
        print("정답입니다!")
        break
    elif n > a:
        print("너무 큽니다. 다시 입력하세요.")
    elif n < a:
        print('너무 작습니다. 다시 입력하세요')