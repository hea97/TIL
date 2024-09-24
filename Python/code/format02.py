# 정수
output_a = "{:d}".format(10)

# 특정 칸 출력
output_b = "{:5d}".format(10)
output_c = "{:10d}".format(10)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(10)
output_e = "{:010d}".format(-10)

print("# 기본")
print(output_a)

print("# 특정 칸 출력")
print(output_b)
print(output_c)

print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)