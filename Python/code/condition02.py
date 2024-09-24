number = input("정수 입력> ")
last_character = number[-1]

if last_character in "02468":
	    print("짝")
if last_character in "13579":
	    print("홀")