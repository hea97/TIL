# 함수 선언
def test():
	print("A 지점 통과")
	yield 1
	print("B 지점 통과")
	yield 2
	print("C 지점 통과")

# 함수 호출
output = test()
# next() 함수 호출
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)
# 한 번 더 실행
next(output)