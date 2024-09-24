# 함수의 기본

함수는 한마디로 ‘코드의 집합’.

---

def 함수 이름():

문장

---

‘코드의 집합’ 목적으로 활용한 것.

### 기본적인 함수

**소스 코드** | `fun_basic.py` 

```python
def print_3_times():
	print("Hello")
	print("Hello")
	print("Hello")

print_3_times()
```

# 함수에 매개변수 만들기

`print()` 함수 작성할 때 `print(value, . . .)`와 같이 괄호 안에 많은 것들 있음.  
→ **매개변수**. 매개변수는 함수를 생성할 때 괄호 내부에 **식별자**를 입력해서 만든다.

---

def 함수 이름(매개변수, 매개변수, . . .)

문장

---

### 매개변수의 기본

**소스 코드** | `param_basic.py` 

```python
def print_n_times(value, n):
	for i in range(n):
		print(value)
print_n_times("Hello", 5)
```

함수 괄호 내부 value n 이라는 식별 입력.  
→ 매개변수

매개변수를 만들면 함수를 호출할 때 값을 입력해서 함수쪽으로 전달할 수 있음.

code에서 print_n_times(”Hello”, 5) 형태로 함수 호출하므로 매개변수 value에는 “Hello” 들어감, 매개변수 n에는 5가 들어감.   
→ “Hello” 5번 출력

# 가변 매개변수

함수 선언할 때 매개변수와 함수 호출할 때의 매개변수가 같아야함.   
적어도 많아도 안됨. 하지만 `print()` 함수는 매개변수를 원하는 만큼 입력. → 매개변수를 원하는 만큼 받을 수 있는 함수를 **가변 매개변수 함수**, 가변 매개변수란 매개변수 개수 변할 수 있다는 의미

가변 매개변수 함수의 형태

---

def 함수 이름(매개변수, 매개변수, . . . *가변 매개변수):

문장

---

가변 매개변수를 사용할 때는 제약이 있음

- 가변 매개변수 뒤 일반 매개변수가 올 수 없음.
- 가변 매개변수는 하나만 사용

제약이 없으면 가변 매개변수가 어디부터 어디까지 알 수 없어 만들어진 규칙.

### 가변 매개변수 함수

**소스 코드** | `variable_param.py` 

```python
def print_n_times(n, *values):
	for i in range(n):
		for value in values:
			print(value)
		print()
print_n_times(3, "Hello", "World", "Python")
```

가변 매개변수 뒤 일반 매개변수 올 수 없다.  
만약 print_n_times("Hello", "World", "Python", 3)처럼 사용 할 수 있다면 매개변수인지 매개변수 n인지 구분하기 힘들어짐.  

따라서 Python에서 내부적으로 가변 매개변수 뒤 일반 매개변수가 오지 못하게 막음

매개변수 n 앞으로 옮기고 매개변수 *values 뒤로 밀었음.  
가변 매개변수 *values 리스트처럼 사용 

# 기본 매개변수

print() 함수 자동 완성 기능.

`print(value, . . ., sep=’ ‘, end=’\n’, file=sys.stdout, flush=False)`

value 바로 ‘가변 매개변수’.  
가변 매개변수 뒤 일반 매개변수 올 수 없다고 했는데 매개변수가 왔음.  
특이하게 ‘매개변수=값’ 형태로 되어 있음. → **기본 매개변수**.

매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본값.

- 기본 매개변수 뒤 일반 매개변수가 올 수 없음.

### 기본 매개변수

**소스 코드** | `default_param.py` 

```python
def print_n_times(value, n=2):
	for i in range(n):
		print(value)
print_n_times("Hello")
```

매개변수 n을 n = 2라는 형태로 입력  
n을 입력하지 않을 경우 기본값 2로 들어감 → Hello라는 문자열 두 번 출력

# 키워드 매개변수

## 기본 매개변수가 가변 매개변수보다 앞에 올 때

기본 매개변수 가변 매개변수보다 앞 올 대는 기본 매개변수의 의미 사라짐.

```python
def print_n_times(n = 2, *values):
	for i in range(n):
		for value in values:
			pirnt(value)
		print()

print_n_times("Hello", "World", "Python")
```

매개변수 순서대로 입력되므로 n에는 “Hello” 들어감, values에는 [”world”, “Python”]이 들어옴. range() 함수 매개변수 숫자만 들어올 수 있으므로 오류 발생

```python
Traceback (most recent call last):
	File "test5_03.py", line 11, in <moudle>
		print_n_times("Hello", "World", "Python")
	File "test.py", line 3, in print_n_times
		for i in range(n):
typeError: 'str' object cannot be interpreted as an integer
```

기본 매개변수는 가변 매개변수 앞 써도 의미 없음

## 가변 매개변수가 기본 매개변수보다 앞에 올 때

반대의 상황 가변 매개변수가 기본 매개변수보다 앞에 올 때

```python
def print_n_times(*valuesn = 2):
	for i in range(n):
		for value in values:
			pirnt(value)
		print()

print_n_times("Hello", "World", "Python", 3)
```

예측

- ["Hello", "World", "Python"] 세 번 출력
- ["Hello", "World", "Python", 3]을 두 번 출력

두 번째 예상 실행. 가변 매개변수가 우선.

---

Hello

world

Python

3

Hello

world

Python

3

---

두 가지 함께 사용 → Python **키워드 매개변수**라는 기능 만들어 놓음.

## 키워드 매개변수

print() 함수 기본 형태

`print(value, . . ., sep=’ ‘, end=’\n’, file=sys.stdout, flush=False)`

value 여러 개 입력 가변 매개변수 앞에 두고, 뒤 기본 매개변수 들어가 있는 형태. 기본 매개변수 지정된 함수 사용할 때 다음과 같이 사용

```python
while True:
	print(".", end="") # 키워드 매개변수
```

매개변수 이름을 직접적으로 지정해서 값을 입력.

### 키워드 매개변수

**소스 코드** | `param_keyword01.py` 

```python
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("Hello", "world", "Python", n=3)
```

매개변수 이름을 지정해서 입력하는 매개변수를 **키워드 매개변수**라고 부른다.

## 기본 매개변수 중에서 필요한 값만 입력하기

키워드 매개변수는 기본 매개변수들로 구성된 함수 많이 사용됨.

### 여러 함수 호출 형태

**소스 코드** | `param_examples.py` 

```jsx
def test(a, b=10, c=100):
	print(a + b + c)

test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)
```

첫 번째 매개변수 a는 일반 매개변수이므로 해당 위치 반드시 입력.    
일반 매개변수 키워드 매개변수처럼 사용

3번형태를 보면 이상함. 매개변수의 순서가 마구잡이로 쓰여 있음.  
키워드를 지정해서 매개변수를 입력하는 경우에는 매개변수 순서 원하는 대로 입력

4번은 b를 생략한 형태.  
키워드 매개변수 사용하면 필요한 매개변수에만 값을 전달

‘일반 매개변수’는 필수로 입력. 순서 맞게 입력. ‘기본 매개변수’는 필요한 것만 키워드 지정해서 입력하는 경우 많음

# 리턴

`input()` 함수.  
`input()` 함수는 함수를 실행하고 나면 다음과 같은 형태로 함수 결과 받아 사용.  
함수의 결과를 **리턴값(return value)**.

```docker
value = input("> ")

pirnt(value)
```

## 자료 없이 리턴하기

함수 내부에서 **return 키워드** 사용.  
이 키워드는 함수를 실행했던 위치로 돌아가라는 뜻, 함수가 끝나는 위치를 의미.

### 자료 없이 리턴하기

**소스 코드** | `return_only.py` 

```python
def return_test():
	print("A 위치")
	return
	print("B 위치")
	
return_test() 
```

함수 내부에서 출력을 두 번 사용했는데 중간에 return 키워드가 들어옴.  
return 키워드는 함수 실행햇떤 위치로 돌아가른 의미와 함수 여기서 끝내라는 의미 가지고 있음.

return 키워드를 만나는 순간 함수 종료되어 결과적으로 “A 위치”만 출력 프로그램 종료

## 자료와 함께 리턴하기

### 자료와 함께 리턴하기

**소스 코드** | `return_with_data.py` 

```python
def return_test():
	return 100
	
value = return_test()
print(value)
```

## 아무것도 리턴하지 않기

### 아무것도 리턴하지 않았을 때의 리턴값

**소스 코드** | `return_none.py` 

```python
def return_test():
	return

value = return_test()
print(value)
```

**None**은 Python에서 ‘없다’란 의미

# 기본적인 함수의 활용

리턴과 관련된 구문 형식.  

---

def 함수(매개변수):

변수 = 초깃값

#여러 가지 처리

#여러 가지 처리

#여러 가지 처리

return 변수

---

### 범위 내부 정수를 모두 더하는 함수

**소스 코드** | `sum_allbasic.py` 

```python
def sum_all(start, end):
    output = 0
    
    for i in range(start, end + 1):
        output += i
    return output

print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))
```

초기값 설정, 연산 해도 값에 아무런 변화 주지 않는 것을 사용.  
e.g. 덧셈식에서는 0. 어떤 값에 0을 더하면 아무런 변화 없음. output 변수 0으로 초기화한 뒤 사용

### 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수

**소스 코드** | `sum_all_with_default.py` 

```python
def sum_all(start=0, end=100, step=1):
	output = 0
	for i in range(start, end + 1, step):
		output += i
	
	return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
```