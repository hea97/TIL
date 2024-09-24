# 숫자 입력 받기
raw_input = input("인치 단위 숫자 입력: ")

# 입력받은 데이터 숫자 자료형 변경, cm 단위로 변경
inch = int(raw_input)
cm = inch * 2.54

# 출력
print(inch, "인치는 cm 단위로", cm, "cm 입니다.")