# 자료형과 기본 자료형

Python 수많은 자료 다룸.  
기능과 역할에 따라 자료 구분, → 구분된 종류를 **자료형(data type)**이라 부름.  
가장 기본적인 자료형 **문자열**, **숫자**, **불**.

- **문자열(string)**
    
    메일 제목, 메시지 내용 등  
    e.g. “Hello World”
    
- **숫자(number)**
    
    물건의 가격, 학생의 성적 등  
    e.g. 10,  1318
    
- **불(boolean)**
    
    로그인 상태 등  
    e.g. True, False
    

기본 자료형을 조합해 새로운 자료형도 만들 수 있음  
e.g. 날짜 표현하는 자료형 ‘2000.00.00’

## 자료를 알아야 하는 이유

자료를 자료형에 맞게 모이고, 처리 과정 거쳐 차근차근 큰 자료형 만들어 나가다 보면 거대한 프로그램 만들어짐. → 가장 기본적인 단위 할 수 있는 자료 의미 아는 것, 쓰임새를 확실하게 아는 것은 매우 중요

## 자료형 확인하기

**자료형(data type)** 자료의 형식.   
Python 자료의 형식을 확인할 때는 **`type()`** 함수 사용. `print()` 함수 식별자 뒤에 괄호 있으므로 함수. 함수의 괄호 내부에 자료 넣으면 그 자료 어떤 자료형 가지고 있는지 확인할 수 있음.

```python
>>> print(type("Hello World"))
<class 'str'>
>>> print(type(10))
<class 'int'>
```

“Hello World”라는 문자열 괄호 안에 넣으니 <class 'str'>, 숫자 괄호 안에 넣으니 <class 'int'> 출력.  
str == string 짧게 표현한 것. → **문자열**

int == integer 짧게 표현한 것 . → **정수**

# 문자열 만들기

`print()` 함수 배우며 “Hello World”이라는 글자 화면에 출력.  
프로그래밍 언어에서 글자 나열된 것을 **문자열**. 문자열은 영어로 **스트링(string)**

| “Hello” | ‘String’ | ‘World’ | “Hello World” |
| --- | --- | --- | --- |

## 큰따옴표로 문자열 만들기

문자열은 문자들을 큰따옴표(”)로 감싸 만듬.  

```python
>>> print("Hello World")
Hello World
```

## 작은따옴표로 문자열 만들기

문자열은 문자들을 작은따옴표(’)로 감싸 만듬.  

```python
>>> print('Hello World')
Hello World
```

## 문자열 내부에 따옴표 넣기

큰따옴표와 작은따옴표를 포함한 문자열 만들기

---

“Hello”World

---

큰따옴표 문자열 내부에 넣고 싶을 때

```python
>>> print('"Hello"World')
"Hello"World
```

작은따옴표 문자열 내부에 넣고 싶을 때

```python
>>> print("'Hello'World")
'Hello'World
```

## 이스케이프 문자를 사용해 문자열 만들기

**이스케이프 문자(escape character**)는 역슬래시(\) 기호와 함께 조합해서 사용하는 특수한 문자 의미. 한국어 키보드에서 \는 원화 기호.

\와 함께 큰따옴표, 작은따옴표 사용 → ‘문자열을 만드는 기호’ 아니라 ‘단순한 따옴표’로 인식

- **\”**
    
    큰따온표 의미
    
- **\’**
    
    작은따옴표 의미
    

이스케이프 문자 사용하면 다음과 같이 큰따옴표 내부 큰따옴표 넣고, 작은따옴표 내부에 작은따옴표 넣을 수 있음.

```python
>>> print("\"Hello\"World")
"Hello"World
>>> print('\'Hello\'World')
'Hello'World
```

그 외 다양한 이스케이프 문자

- **\n**
    
    줄바꿈 의미
    
- **\t**
    
    탭 의미
    

```python
>>> print("Hello\nHello")
Hello
Hello
>>> print("Hello\tHello")
Hello	Hello
```

### 이스케이프 문자(\t)로 탭 사용하기

**소스 코드** | `string_operator.py` 

# 소스 코드 | string_operator.py

```python
print("Hello\tWorld")
print("hea97\tPython")
print("Python\tcode")
```

Hello World

hea97 Python

Python code

- **\\**
    
    역슬래시(\)를 의미
    

```python
>>> print("\\ \\ \\ \\")
\ \ \ \
```

## 여러 줄 문자열 만들기

\n 사용 줄바꿈

```python
>>> print("Hello\nWorld\nhea97\nPython\nPython\ncode")
Hello
World
hea97
Python
Python
code
```

**문제점** | 이 코드에 문제점은 한 줄에 긴 코드에 입력하면 읽기가 힘들뿐 아니라 한 줄에 줄바꿈 문자도 많아 어떤 부분 줄바꿈이 일어나는지 확인 번거롭고 \n를 하나하나 찾아야함

Python은 **여러 줄 문자열** 기능 지원.  
큰따옴표 또는 작은따옴표를 세 번 반복한 기호를 사용

```python
>>> print("""Hello World hea97 
Python 
Python code""")
Hello World hea97 
Python 
Python code
```

큰따옴표 또는 작은따옴표 세 번 반복한 후 문자열 입력하면 | Enter | 누르는 곳마다 줄바꿈이 일어남 → 더 쉽게 읽을 수 있음

## 줄바꿈 없이 문자열 만들기

```python
>>> print("""
Hello World hea97 
Python Python code
""")

Hello World hea97 
Python Python code

```

의도하지 않은 줄바꿈 들어감 → 들어가지 않게 할려면 **\ 기호** 사용.  
Python 코드 쉽게 보려고 줄바꿈한 것이지 실질적인 줄바꿈이 아니라는것을 나타냄. 줄 뒤에 \ 기호 사용

```python
>>> print("""\
Hello World hea97 
Python Python code\
""")
Hello World hea97 
Python Python code
```

---

**note** | \ 기호 여러 줄 문자열을 사용할 때뿐만 아니라 다양한 상황 활용 기호

---

# 문자열 연산자

숫자에 더하기, 빼기, 곱하기, 나누기 연산자, 합집합, 교집합, 차집합 등 연산자 적용

‘숫자’라는 자료에 더하기, 빼기, 곱하기, 나누기라는 연산자 적용 가능.  
합집합, 교집합, 차집합이라는 연산자는 적용 X. → 각각 자료는 사용할 수 있는 연산자가 정해져 있습니다.

## 문자열 연결 연산자 : +

문자열 **+ 연산자** 문자열 연결 연산 적용

> “문자열” + “문자열”
> 

 + 기호 사용. ‘숫자 더하기 연산자’와 ‘문자열 연결 연산자’는 + 기호를 사용하지만, 내부적으로는 다르게 수행하는 연산자이다

**문자열 연결 연산자**는 문자열 연결해서 새로운 문자열을 만듬.  

```python
>>> print("Hello" + "World")
Hello World
>>> print("Hello" + "!!")
Hello!!
```

## 문자열 반복 연산자 : *

문자열 숫자와 *** 연산자** 연결하면 문자열 반복.  
**문자열*숫자** 순으로 입력,

```python
>>> print("Hello" * 10)
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
```

**숫자*문자열** 순서를 바꿔 입력.  
**문자열 반복 연산자**는 문자열 숫자만큼 반복해서 출력함

```python
>>> print(10 * "Hello")
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
```

## 문자 선택 연산자(인덱싱) : []

**문자 선택 연산자** 문자열 내부 문자 하나 선택하는 연산자.  
대괄호[] 안 선택할 문자의 위치 지정, 숫자를 **인덱스(Index)**라고 함.

인덱스 유형 두 가지 구분해 사용.

1. 숫자를 0부터 세는 **제로 인덱스(zero Index)**
2. 숫자 1부터 세는 **원 인덱스(one Index)**

로 구분.  
Python은 ‘제로 인덱스’ 유형 사용하는 언어. 즉 문자열 위치를 셀 때 무조건 0부터 세어 첫번째 글자 0번째, 두 번째 글자가 1번째가 된다.

e.g.

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| [0] | [1] | [2] | [3] | [4] |

### 문자 선택 연산자의 결과 출력하기

**소스 코드** | `string_operator01.py`

# 소스 코드 | string_operator01.py

```python
print("문자 선택 연산자")
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
```

코드를 실행시키면 0부터 시작하므로   
0번째 ‘H’ 4번째 ‘o’가 나온다.

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| [0] | [1] | [2] | [3] | [4] |

### 뒤에서부터 선택하기

**소스 코드** | `string_operator02.py`

# 소스 코드 | string_operator02.py

```python
print("문자 선택 연산자")
print("Hello"[-5])
print("Hello"[-4])
print("Hello"[-3])
print("Hello"[-2])
print("Hello"[-1])
```

숫자를 음수로 입력하면 뒤에서부터 선택할 수 있음.

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| [-5] | [-4] | [-3] | [-2] | [-1] |

## 문자열 범위 선택 연산자(슬라이싱) : [:]

문자열 특정 범위 선택 사용 연산자.  
e.g. 문자열 첫 번째 문자부터 세 번째 문자까지 선택, 두 번째 문자부터 끝까지 선택한다든지 **범위** 지정**.**  
범위는 대괄호 안 위치를 콜론(:)으로 구분해서 지정

```python
 >>> print("Hello"[1:4])
 ell
```

프로그래밍 언어 따라 두 가지 유형.

1. 범위 지정 시 ‘마지막 숫자를 포함’
2. ‘마지막 숫자를 포함하지 않음’

Python은 ‘마지막 숫자 포함하지 않음’ 적용   
위와 같은 코드 입력 시 1번째 + 2번째 + 3번째 글자까지만 추출되어 “ell” 출력

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| [0] | [1] | [2] | [3] | [4] |

→

|  | e | l | l |  |
| --- | --- | --- | --- | --- |
|  | [1] | [2] | [3] |  |

다른 예제

```python
>>> print("Hello"[0:2])
He
>>> print("Hello"[1:3])
el
>>> print("Hello"[2:4])
ll
```

[0:2]라고 입력하면 (뒤의 숫자)번째까지 선택 X.  
(뒤의 숫자 -1)번째까지 선택.  
[0:2]는 0번째 글자부터 1번째 글자를 선택, 0번째부터 2번째 추출 하는 것 아니므로 주의

**문자열 범위 선택 연산자** 대괄호 안 넣는 숫자 둘 중 하나 생략  
뒤 값 생략할 때는 자동으로 가장 최대 위치(마지막 글자)까지, 앞의 값 생략할 때는 가장 앞쪽의 위치(첫 번쨰 글자)까지 지정

---

[1:]

[:3]

---

[1:] 경우 뒤 값 생략 때문에 1번째부터 끝의 문자 선택, [:3]의 경우 앞의 값 생략 0번째부터 뒤 숫자 3번째 앞의 문자까지 선택.

```python
>>> print("Hello"[1:])
ello
>>> print("Hello"[:3])
Hel
```

문자열 원하는 위치 지정해 문자를 분리.  
→ **[] 연산자** 이용 문자열 특정 위치 있는 문자 참조하는 것을 **인덱싱(Indexing)**, **[:] 연산자** 이용 문자열 일부 추출하는 것을 **슬라이싱(slicing)**.

---

**note |** 문자열과 관련된 연산자 리스트에도 적용. 사용 빈도 높은 편

---

# 문자열의 길이 구하기

문자열 길이 구할 때 **`len()`**  함수 사용.  

괄호 내부에 문자열을 넣으면 ‘문자열 들어있는 문자 개수(= 문자열의 길이)’를 세어 준다  
Hello라는 문자열은 다섯 글자이므로 5 출력

```python
>>> print(len("Hello"))
5
```

현재 코드에서 함수 이중으로 사용. → 함수가 여러 번 중첩되어 사용되면 괄호 안쪽 먼저 실행.