nubmer = input("정수 입력> ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 \
	    or last_number == 2 \
	    or last_number == 4 \
	    or last_number == 6 \
	    or last_number == 8:
	    print("짝")
if last_nubmer == 1 \
	    or last_number == 3 \
	    or last_number == 5 \
	    or last_number == 7 \
	    or last_number == 9:
	    print("홀")