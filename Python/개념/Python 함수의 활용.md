# 재귀 함수

팩토리얼(factorial)이라는 연산자. 

`n! = n * (n - 1) * (n - 2) * . . . * 1`

팩토리얼 구하는 방법 두 가지

- 반복문으로 팩토리얼 구하기
- 재귀 함수로 팩토리얼 구하기

## 반복문으로 팩토리얼 구하기

반복문으로 팩토리얼을 구하는 방법.  
start부터 end까지 더하는 함수를 곱하는 함수로 바꾸기만하면 됨.

### 반복문으로 팩토리얼 구하기

**소스 코드** | `factorial_for.py` 

```python
def factorial(n):
	output = 1
	for i in range(1, n + 1):
		output *= i 
	return output

print("1! :", factorial(1))
print("2! :", factorial(2))
print("3! :", factorial(3))
print("4! :", factorial(4))
print("5! :", factorial(5))
```

초기값은 로 설정, 어떤 값이라도 1을 곱하면 변화가 없기 때문에 1로 설정. 

## 재귀 함수로 팩토리얼 구하기

두 번째 방법 **재귀 함수** 사용하는 방법.  
재귀(recursion)란? ‘자기 자신을 호출하는 것’ 의미

`n! = n * (n - 1) * (n - 2) * . . . * 1`

표현

`factorial(n) = n * factorial(n - 1) (n ≥ 1일 때)`

`factorial(0) = 1`

재귀 표현 이용 factorial(4) 구해 보기

```python
f(4) = 4 * f(3)
     = 4 * 3 * f(2)
     = 4 * 3 * 2 * f(1) * f(0)
     = 4 * 3 * 2 * 1 * 1
```

### 재귀 함수를 사용해 팩토리얼 구하기

**소스 코드** | `factorial_recursion.py` 

```python
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))
```

# 재귀 함수의 문제

재귀 함수는 상황 따라 기하급수적 많이 반복한다는 문제.  
필요할 때 적재적소 활용하면 코드 쉽게 알아볼 수 있음.  
재귀 함수 인해 발생하는 문제와 문제를 해결하는 **메모화(memoization)**라는 기술

피보나치 수열.  
피보나치 수열은 ‘토끼는 어떠한 속도로 번식하는가’와 같은 연구에 사요오디는 사용되는 수열

- 처음에는 토끼가 한쌍만 존재
- 두 달 이상 된 토끼는 번식
- 번식 가능한 토끼 매달 새끼를 한 쌍씩 낳음
- 토끼는 죽지 않는다 가정

달이 지날 수록 1쌍에서 nn쌍. . .

- 1번째 수열 = 1
- 2번째 수열 = 1
- n번째 수열 = (n - 1)번째 수열 + (n - 2)번째 수열

### 재귀 함수로 구현한 피보나치 수열(1)

**소스 코드** | `fibonacci_recursion01.py` 

```python
def fibonacci(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
		
print("fibonacci(1) : ", fibonacci(1))
print("fibonacci(2) : ", fibonacci(2))
print("fibonacci(3) : ", fibonacci(3))
print("fibonacci(4) : ", fibonacci(4))
print("fibonacci(5) : ", fibonacci(5))
```

### 재귀 함수로 구현한 피보나치 수열(2)

**소스 코드** | `fibonacci_recursion02.py` 

```python
counter = 0

def fibonacci(n):
	print("fibonacci({})를 구함.".format(n))
	global counter
	counter += 1
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
	
fibonacci(10)
print("---")
print("fibonacci(10) 계산 활용된 덧셈 횟수는 {}번.".format(counter))
```

`fibonacci(10)` 구하는데 109번 연산

숫자를 바꾸면서 코드 몇 번 더 실행해 보면 35번째 피보나치 수 구할 때 덧셈 무려 18454929번이나 반복 계산.

`fibonacci(35) 계산에 활용된 덧셈 횟수 18454929번`

덧셈 횟수 기하급수적으로 늘어나는 이유.  
**트리(tree)**, 트리에 있는 각각의 지점을 **노드(node)**, 노드 중 마지막 단계 노드 **리프(leaf)**

트리 내부 있는 각각 노드 값 계산하려면 덧셈 한 번씩 해야함.  
노드가 한 번에 두 개씩 달려 있음, 한 번 구한 값은 그것으로 계산이 끝나면 좋겠지만, 코드의 재귀 함수는 한 번 구했던 값이라도 처음부터 다시 계산. 계산 횟수 기하급수적 늘어나는 것

## UnboundLocalError에 대한 처리

### 재귀 함수로 구현한 피보나치 수열(3)

**소스 코드** | `fibonacci_recursion03.py` 

```python
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
```

코드  실행 시 **UnboundLocalError** 예외 출력

Python 함수 내부 함수 외부에 있는 변수 참조하지 못함.  
변수에 접근하는 것을 **참조(reference)**라고 부름 함수 내부 함수 외부에 있는 변수.

`global 변수 이름`

**global 키워드** Python 프로그래밍 언어 특이한 구조.  
필자드 global 키워드 존재 전혀 생각하지 않고 코드 작성할 때 많음.  
`W0621: Redefining name ‘counter’ from outer scope` 또는 `E0602: Undefined bariable` ‘conuter’ 나타나면 그제야 global 키워드 쓰라는 것 판단 코드 수정

## 메모화

재귀 함수의 이러한 문제 때문에 재귀 함수 사용하지 말라는 개발자 있음.  
필요 경우 활용하면 코드가 간결해지며 읽기 쉬워짐.

문제는 같은 값을 구하는 연산을 반복하고 읽기 때문에 발생 하는 것.   
→ 같은 값을 한 번만 계산하도록 코드 수정.

### 메모화

**소스 코드** | `fibonacci_memo.py` 

```python
dictionary = {
	1 : 1,
	2 : 1
}

def fibonacci(n):
	if n in dictionary:
		return dictionary[n]
	else:
		output = fibonacci(n - 1) + fibonacci(n - 2)
		dictionary[n] = output
		return output

print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(20) : ", fibonacci(20))
print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))
print("fibonacci(50) : ", fibonacci(50))
```

딕셔너리 사용해 한 번 계산한 값 저장.  
**메모(memo)**한다고 표현. 딕셔너리 값이 메모되어 있으면 처리 수행하지 않고 곧바로 메모된 값을 돌려주면서 코드 속도 빠르게 만드는 것

e.g.  
`fibonacci(50)` 계산 한참 걸렸음, **메모화**를 사용하면 실행 후 곧바로 결과 출력할 정도로 속도 빨라짐. 

# 조기 리턴

프로그래밍 할 때 변수 반드시 앞쪽 몰아서 선언, 리턴은 반드시 뒤쪽 해야한다는 비공식적 규칙 있음.

```python
def fibonacci(n):
	if n in dictoinary:
		return dictionary[n]
	else:
		output = fibonacci(n - 1) + fibonacci(n - 2)
		dictionary[n] = output
		return output
```

들여쓰기 단계가 줄기 때문에 코드 더 쉽게 읽을 수 있음.  
흐름 중간에 return 키워드 사용하는 것을 **조기 리턴(early retums)**이라고 부름

```python
def fibonacci(n):
	if n in dictionary:
		return dictionary[n]
	output = fibonacci(n - 1) + (n - 2)
	dictionary[n] = output
	return output
```

# 리스트 평탄화하는 재귀 함수 만들기

**리스트 평탄화**  
중첩된 리스트 있을 때 중첩을 모두 제거 풀어서 1차원 리스트로 만드는 것을 의미.

`[[1, 2, 3], [4, 5, 6], 7, [8, 9]]`  → `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

2차원 리스트 평탄화,  
몇 차원까지 중첩될지 정해지지 않은 리스트 평탄화 문제 조금 어려움.

리스트 하나 입력 받아 → 평탄화해서 **리턴**하는 함수 만듬.  
`flatten`이라는 이름 재귀 함수의 기본 구조 잡아 생성

```python
def flatten(data):
	output = []
	
return output
```

내부 있는 요소 하나씩 확인 리스트인지 리스트 아닌지 확인.  
요소 하나씩 확인하는 **for 반복문** 추가

```python
def flatten(data):
	output = []
	for item in data:
	
return output
```

for 반복문 내부 리스트인지 리스트가 아닌지 확인해야함.  
리스트 아니라면 바로 `output` 리스트 자료 넣고, 리스트라면 리스트에 있는 요소들을 하나하나 `output` 추가해야함

```python
def flatten(data):
	output = []
	for item in data:
		if type(item) == list:
		
		else:
			output.append(item)
return output
```

리스트 있는 내용 추가할 때는 + 연산자 또는 extend() 함수 사용, 여기에서는 **+ 연산자** 사용

### 리스트 평탄화하기(1)

**소스 코드** | `list_flatten01.py` 

```python
def flatten(data):
	output = []
	for item in data:
		if type(item) == list:
			output += item
		else:
			output.append(item)
	return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example))
```

### 리스트 평탄화하기(2)

**소스 코드** | `list_flatten02.py` 

```python
def flatten(data):
	output = []
	for item in data:
		if type(item) == list:
			output += flatten(item)
		else:
			output.append(item)
	return output
	
example = [[1, 2, 3], [4 ,[5, 6], 7, [8, 9]]]
print("원본 : ", example)
print("변환 : ", flatten(example))
```

### 첫째, 함수의 변수는 함수 호출마다 따로따로 만들어집니다.

`flatten()` 함수 `flatten()` 함수를 호출할 때 변수 `output` 계쏙해서 이어진다 생각 경우. 함수의 변수는 함수 호출마다 따로 만들어짐.

### 둘째, 함수가 끝나면(리턴되면) 함수를 호출했던 위치로 돌아옴

`output += flatten(item)`부분 재귀적으로 `flatten()`  함수 호출

# 코드에 이름 붙이기

가독성.  
가독성이란 코드를 쉽게 읽을 수 있는 성질이라 정의.  
즉 가독성이 좋은 코드는 쉽게 읽을 수 있다는 의미.

가독성은 프로그래밍할 때 굉장히 중요한 요소.  
프로그래밍 성능과 속도만 주용하다면 모든 프로그램이 C언어로 개발되었을 것. 파지만 C 언어는 ‘학습 난이도가 높다’, ‘가독성 좋게 코드를 작성하기 힘들다’라는 단점이 있다. 못하는 것은 아니다.  
가독성 좋게 코드를 작성할 수 있는 상급자 될 때까지 걸리는 시간, 노력 크다는 것,

함수 가독성 좋은 코드 작성하는 방법.  
코드 2 * 3.14 * radius와 3.14 * radius * radius와 같은 식 있으니 원 둘레와 넓이를 구한다고 생각할 수 있지만, 무엇을 나타내는 함수인지 생각해내는데 시간이 걸림

**어떠한 설명 없는 코드**

```python
number_input_a = input("숫자 입력> ")
radius = float(number_input_a)

print(2 * 3.14 * radius)
print(3.14 * radius * radius)
```

**주석이 있는 코드**

```python
# 숫자 입력 받기
number_input_a = input("숫자 입력> ")
radius = float(number_input_a)

# 원의 둘레 넓이를 출력
print(2 * 3.14 * radius)
print(3.14 * radius * radius)
```

‘주석 잘 사용하는 사람 프로그램이 잘하는 사람.’ 주석을 잘 사용할 수록 다른 사람과 함께 프로그램 작성할 떄 가독성 좋아지기 때문.  
그렇다고 주석 남발..? X. 필요한 경우에만 정확하게 사용하는 것이 좋음

함수를 코드에 이름을 붙일 수 있음. 코드에 이름을 붙이면 쉽게 읽을 수 있음. 다음 코드 보면 주석 없어도 코드 쉽게 읽을 수 있음(area와 circumference라는 단어 의미 모르면 힘듬)

**함수를 활용한 코드**

```python
# 함수 정의
def number_input():
	output = input("숫자 입력> ")
	return float(output)
def get_circumference(radius):
	return 2 * 3.14 * radius
def get_circle_area(radius)
	return 3.14 * radius * radius

# 코드 본문
radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius))
```

함수 부분은 생략하고 코드 본문 부분만 살펴본다면 주석 없이 코드만 읽고 무엇을 하는 코드인지 쉽게 알 수 있음

```python
redius = number_input()
print(get_circumference(radius))
print(get_circle_are(radius))
```

한 줄의 코드라도 의미 가지고 있다면 함수로 만드는 것이 좋음.  
함수 부분은 **모듈(module)** 기능으로 더 간단하게 만들 수 있음

# 코드 유지보수

함수 활용 코드 유지보수 할 때 도움 됨.  
함수는 코드 이름 붙인다는 점 변수와 비슷, 일반 변수로 유지보수 좋게 하는 방법 알아보고 함수 활용.

**3.14를 숫자로 입력한 상태**

```python
def get_circumference(radius):
	return 2 * 3.14 * radius
def get_circle_area(radius):
	return 3.14 * radius * radius
```

변수로 만들어 가독성 높여줄 수 있음

**3.14를 PI라는 변수로 설정한 상태**

```python
PI = 3.14

def get_circumference(radius):
	return 2 * PI * radius
def get_circle_area(radius):
	return PI * radius * radius
```

장점.

기존의 상태에서 3.14 숫자 찾아 하나하나 변경하거나 전체 수정 해야할 것. 변수PI 옆 3.14라는 숫자를 3.141592로만 수정

**함수를 사용하지 않은 경우**

```python
# 출력
print("<p>{}</p>".format("Hello"))
print("<p>{}</p>".format("간단한 HTML 태그 만드는 예시"))
```

갑자기 요청으로 “<p></p> 감싸지 말고 <p class=’content-line’></p> 감싸줘”라는 요청 받았다면 어떻게 해야할까? 함수 사용하지 않은 상태 모든 코드 하나하나 수정. 당연히 실수 등 발생 하지만 함수 사용 이러한 수정 쉽게 할 수 있음 해당 함수만 변경.  
함수를 사용하면 요청사항 등이 있을 때 쉽게 반영

```python
def p(content):
	# return "<p>{}</p>".format(content)
	return "<p class=’content-line’>{}</p>".format(content)

print("<p>{}</p>".format("Hello"))
print("<p>{}</p>".format("간단한 HTML 태그 만드는 예시"))
```