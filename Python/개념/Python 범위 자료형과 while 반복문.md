# 범위

리스트, 딕셔너리 외 for 반복문 함께 많이 사용되는 **범위(range)** 자료형 사용법. 정수로 이루어진 범위 만들 때는 **`range()`** 함수 사용

### 1. 매개변수에 숫자를 한 개 넣는 방법

0부터 A-1까지 정수 범위 만듬

`range(A)` → A는 숫자

### 2. 매개변수에 숫자를 두 개 넣는 방법

A부터 B-1까지 정수로 범위 만듬

`range(A, B)` → A와 B 숫자

### 3. 매개변수에 숫자를 세 개 넣는 방법

A부터 B-1까지 정수 범위 만듬, 앞 뒤의 숫자가 C 만큼의 차이 가진다

`range(A, B, C)` → A, B, C 숫자

---

매개변수 한 개 넣는 방법. 범위 선언

```python
>>> a = range(5)
```

```python
>>> a
range(0, 5)
```

어떤 값 해당하는지 보지 위해 **`list()`** 함수 출력.  
`list()` 함수 이용해 범위 리스트 변경하면 범위 내부 어떤 값 들어 있는지 확인

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

매개변수 두 개 넣은 범위

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
```

매개변수 세 개 넣은 범위

```python
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
```

범위 만들 때 매개변수 내부 수식 사용하는 경우 많음.  
e.g. 0부터 10까지 범위 생성, 10을 반드시 포함해야 한다는 것 강조하고 싶을 때

```python
>>> a = range(0, 10 + 1)
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

11을 굳이 10+1로 표현하는 것 비효율적 같지만.  
정확하게 콕 집어 강조할 수 있음

수식에 나누기 연산자 사용한 경우

```python
>>> n = 10
>>> a = range(0, n / 2)
Traceback (most recent call last):
	FIle "<pyshell#10>, line 1, in <module>"
TypeError: 'float' object cannot be interpreted as an integer
```

**TypeError** 발생하는 이유 `range()` 함수 매개변수 반드시 ‘정수’ 입력.  
`int()` 함수 등 실수 정수 바꾸는 방법.

```python
# 실수 정수로 바꾸는 방법
>>> a = range(0, int(n / 2))
>>> list(a)
[0, 1, 2, 3, 4]

# 정수 나누기 연산자 많이 사용
>>> a = range(0, n // 2)
>>> list(a)
[0, 1, 2, 3, 4]
```

# `for` 반복문 : 범위와 함께 사용하기

`for` 반복문 범위 조합하는 방법.  
`for` 반복문 범위 조합해서 사용하면 다음 형태

---

for 숫자 변수 in 범위:

코드

---

### for 반복문과 범위

**소스 코드** | `for_range.py` 

```python
for i in range(5):
	print(str(i) + "= 반복 변수")
print()

for i in range(5, 10):
	print(str(i) +  "= 반복 변수")
print()

for i in range(0, 10, 3):
	print(str(i) +  "= 반복 변수")
print()
```

첫 번째 반복문 [0, 1, 2, 3, 4], 두 번째 반복문 [5, 6, 7, 8, 9], 세 번째 반복문 [0, 3, 6, 9]

# `for` 반복문 : 리스트와 범위 조합하기

```python
array = [25, 45, 95, 123, 40]

for element in array:
	print(element)
```

### 리스트와 범위를 조합해서 사용하기

**소스 코드** | `list_range01.py` 

```python
array = [25, 45, 95, 123, 40]

for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))
```

가장 기본적이고 많이 사용되는 형태.

# `for` 반복문 : 반대로 반복하기

프로그래밍 하다 보면 반복 변수 큰 숫자에서 작은 숫자로 반복문 적용해야 하는 경우. 이런 반복문을 **역반복문**.

1. **`range()`** 함수 매개변수 세 개 사용 방법

### 반대로 반복하기(1)

**소스 코드** | `reversed_for01.py` 

```python
for i in range(4, 0 - 1, -1):
	print("현재 반복 변수 : {}".format(i))
```

range() 함수 매개변수 0 - 1 수식.  
그냥 -1 입력 상관 없음. “0까지 반복하고 싶어서 이 코드 사용” 강조

1. **`reversed()`** 함수 사요하는 방법

### 반대로 반복하기(2)

**소스 코드** | `reversed_for02.py` 

```python
for i in reversed(range(5)):
	print("현재 반복 변수 : {}".format(i))
```

reversed() 함수 적용 [0, 1, 2, 3, 4] 형태 범위가 [4, 3, 2, 1, 0] 뒤집어짐.  
9부터 0까지 반대로 반복문 돌릴 수 있음

`reversed()` 함수 리스트 등 적용.  
`reversed()` 함수 처음 사용하다보면 주의 사항이 많이 피룡한 함수.

# `while` 반복문

리스트 또는 딕셔너리 내부 요소 모두 순회, 특정 횟수만큼 반복하는 경우 `for` 반복문 사용.  
Python `for` 반복문 외에 범용적으로 사용할 수 있는 **`while` 반복문** 있음.

기본적 형태

---

while 불  표현식:

문장

---

if 조건문과 비슷한 형식, <불 표현식> 참인 동안 문장을 계속 반복.  

### 누적 예제 | 중첩 반복문으로 피라미드 만들기

**소스 코드** | `for_pyramid01.py` 

```python
output = ""

for i in range(1, 10):
	for j in range(0, i):
		output += "*"
	output += "\n"

print(output)
```

Python 튜더 활용. `output`, `i`,  `j` 변수

**소스 코드** | `for_pyramid02.py` 

```python
output = ""

for i in range(1, 15):
	for j in range(14, i -1):
		output += ''
	for k in range(0, 2 * i - 1):
		output += '*'
	output+= '\n'

print(output)
```

### 무한 반복

**소스 코드** | `infinite_loop.py` 

```python
while True:
	# "." 출력
	# 기본적으로 end가 "\n" 줄바꿈 일어남
	# 빈 문자열 "" 바꿔서 줄바굼 일어나지 않게 함
	print(".", end="")
```

실행하면 위와 같이 화면에 “.”이 무한 반복 출력. 때문에 강제 종료 해줘야함.

```python
..............................................................
..............................................................
..............................................................
..............................................................
..............................................................
```

# `while` 반복문 : `for` 반복문처럼 사용하기

### while 반복문을 for 반복문처럼 사용하기

**소스 코드** | `while_as_for.py` 

```python
i = 0
while i < 10:
	print("{}번째 반복.".format(i))
	i += 1
```

`for`, `while` 반복문 어떻게 나누어 사용?    
모두 `while` 반복문 사용. 대표적으로 무한 반복, `for` 반복문으로는 **무한 반복**을 구현할 수 없음. `while` 반복문에서 가장 중요한 키워드는 **조건**. 조건을 활용해서 반복 사용 → while 반복문 사용하는 것이 좋음

# while 반복문 : 상태를 기반으로 반복하기

리스트의 `remove()` 함수 내부 해당하는 값 하나만 제거할 수 있음.  
`while` 반복문을 활용하면 여러 개 제거 가능.   
`while` 반복문 조건 ‘리스트 내부 요소 있는 동안’ 지정

### 해당하는 값 모두 제거하기

**소스 코드** |  `while_with_condition.py` 

```python
list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
	list_test.remove(value)
	
print(lsit_test)
```

# while 반복문 : 시간을 기반으로 반복하기

시간 기반 반복하는  
시간을 기반으로 반복할려면 유닉스 타임이라는 개념 알아야함.  
**유닉스 타임(Unix Time)**이란 세계 표준시(UTC)로 1970년 1월 1일 0시 0분 0초 기준으로 몇 초 지낫는지 정수로 나타낸 것을 말함.

시간과 관련된 기능 가져옴

```python
>>> improt time
```

유닉스 타임

```python
>>> time.time()
1557241486.6654928
```

### 5초 동안 반복하기

**소스 코드** |  `while_with_time.py` 

```python
import time

number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
	number += 1
	
print("5초 동안 {}번 반복".format(number))
```

# while 반복문 : break 키워드/continue 키워드

반복문 내부에서만 사용할 수 있는 `break`와 `continue`라는 특수한 키워드.  
**break 키워드** 반복문 벗어날 때 사용하는 키워드. 일반적으로 무한 반복문을 만들고, 내부 반복을 벗어날 때 많이 사용한다

### break 키워드

**소스 코드** |  `break.py` 

```python
i = 0

while True:
	print("{}번째 반복".format(i))
	i = i + 1
	input_text = input("> 종료하시겠습니까?(y/n) : ")
	if input_text in ["y", "Y"]:
		print("반복 종료")
		break
```

“0번째 반복문” 출력 프로그램 종료.  
”y” 또는 “Y” 입력 break 키워드 만나 반복문 벗어나게 되므로 프로그램 종료. 이 외 경우에는 반복문 계속 실행

### continue 키워드

**소스 코드** |  `break01.py` 

```python
numbers = [5, 15, 4, 20, 7, 25]

for number in numbers:
	if number < 10:
		continue
	print(number)
```

현재 코드 if else 구문 사용해도 됨.  
continue 키워드 사요하면 이후 처리 들여쓰기를 하나 줄일 수 있음

### continue 키워드 사용하지 않은 경우

```python
for number in numbers:
# 반복 대상 한정
	if number >= 10:
		#문장
		#문장
		#문장
		#문장
		#문장
```

### continue 키워드 사용한 경우

```python
for number in numbers:
# 반복 대상 제외
	if number < 10:
	#문장
	#문장
	#문장
	#문장
	#문장
```