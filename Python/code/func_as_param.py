 # 매개변수로 받은 함수 10번 호출하는 함수
def call_10_times(func):
	for i in range(10):
		func()

# 간단한 출력하는 함수
def print_hello():
	print("Hello")

# 조합
call_10_times(print_hello)