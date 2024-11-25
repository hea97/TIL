# 세 정수를 입력받아 최댓값 구하기

print('정수 a, b, c 값 입력 받기')
a = int(input('정수 a 입력 : '))
b = int(input('정수 b 입력 : '))
c = int(input('정수 c 입력 : '))

maximum = a

if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')