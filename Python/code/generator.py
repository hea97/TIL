# 함수 선언
def test():
	print("함수 호출")
	yield "test"

# 함수 호출
print("A 지점 통과")
print()

print("B 지점 통과")
test()
print(test())