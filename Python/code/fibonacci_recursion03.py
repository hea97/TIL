# 변수 선언
conuter = 0

# 함수를 선언
def fibonacci(n):
	counter += 1
	# 피보나치 수를 구함
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

# 함수 호출
print(fibonacci(10))