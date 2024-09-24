# 문장

실행할 수 있는 코드 최소 단위 **문장(statement)**.  
Python ‘한 줄 하나의 문장’. 문장들이 모이면 **프로그램(program)** 

```python
# 실행되는 모든 한 줄 코드 문장
print("Hello, World")
# 문장
```

# 표현식

Python 어떠한 값 만들어 내는 간단한 코드 **표현식(expression)**.   
→ 숫자, 수식, 문자열 등과 같은 것을 의미

```python
273
10 + 20 + 30 * 10
"Hello, World"
```

+, - 는 표현식이 아니다.

# 키워드

**키워드(keyword)** 특별한 의미가 부여된 단어로  Python 만들어질 때 이미 사용하겠다 예약해 놓은 것.  
사용자는 키워드인지 아닌지 구분해야하는 유는 프로그래밍 언어에서 사용자가 이름을 정할 때 사용하면 안 되기 때문이다

### Python keyword

|  False | None | True | and | as | assert |
| --- | --- | --- | --- | --- | --- |
| async | await | break | class | continue | def |
| del | elif | else | except | finally | for |
| from | global | if  | import | in | ls |
| Iambda | nonlocal | not | or | pass | raise |
| retum | try | while | with | yield |  |

# Python 키워드 확인 code

```python
>>> import keyword
>>> print(keyword.kmlist)
```

# Python 키워드

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
'try', 'while', 'with', 'yield']
```

이 단어들은 변수, 함수, 클래스 이름으로 사용할 수 없다.

Python은 대소문자 구분.  
e.g. True == 키워드, true == 키워드 X. 즉 true로는 이름 정할 수 없고 true.는 이름을 정할 수 있음.

---

**note** | code 전용 에디터 사용해 보면 code 입력할 때 일반적인 단어 흰색 or 검은색 표시 키워드들의 경우 특별한 색상으로 들어아기 때문에 쉽게 구분

---

# 식별자

**식별자(identifier)**는 프로그래밍 언어 이름을 붙일 때 사용하는 단어.  
주로 변수 or 함수 이름등으로 사용

기본적인 규칙

- 키워드 사용하면 안됨
- 특수 문자 언더바(_)만 허용
- 숫자로 시작하면 안됨
- 공백을 포함할 수 없음

규칙에 맞는 단어 모두 식별자로 사용.  
e.g. 왼쪽에는 모두 식별자로 사용 가능, 오른쪽에는 모두 식별자로 사용 X.

| 사용 가능한 단어 | 사용 불가능한 단어 |
| --- | --- |
| aipha | break #키워드라서 안됨 |
| alpha10 |  |
| _alpha | 273alpha #숫자로 시작해서 안됨 |
| AlpHa |  |
| ALPHA | has space #공백을 포함해서 안됨 |

식별자 만들 때 전세계 언어 모두 사용,  하지만 알바펫을 사용하는 것이 관례. 또한 a, b 의미 없는 단어 보단 file, output 처럼 의미 있는 단어 사용 하는 것이 좋음.

## 스네이크 케이스와 캐멀 케이스

식별자 공백 사용 X.

| itemlist | loginstatus | characterhp | rotateangle |
| --- | --- | --- | --- |

이해하기 쉽게 하기 위해 두 가지 방법

### 스네이크 케이스(snake_case)

e.g. `itemlist`를 `item_list` → **스네이크 케이스(snake_case)**

### 캐멀 케이스(CameCase)

e.g. `itemlist`를 `ItemList` → **캐멀 케이스(CameCase)**

| 식별자 공백 없는 경우 | 단어 사이에 _ 기호 붙인 경우 (스네이크 케이스) | 단어 첫 글자 대문자 만든 경우 (캐멀 케이스) |
| --- | --- | --- |
| itemlist | item_list | ItemList |
| loginstatus | login_status | LoginStatus |
| characterhp | character_hp | CharacterHp |
| rotateangle | rotate_angle | RotateAngle |

스네이크 케이스는 글자들이 뱀처럼 연결 == **스네이크 케이스**

캐멀 케이스는 글자들이 낙타 같다고 해서 == **캐멀 케이스**

대부분 프로그래밍 언어 둘 중 하나 사용.  
Python의 경우 두 가지 모두 사용.

## 식별자 구분하기

캐멀 케이스 ‘첫 번째 글자로 대문자로 적는다’와 ‘첫 번째 글자를 소문자로 적는다’ 구분.  
Python은 ‘첫 번째 글자를 소문자로 적는다’라는 캐멀 케이스 사용 X.

---

캐멀 케이스 유형 1 : PrintHello → Python 사용.

캐멀 케이스 유형 2 : printHello → Python 사용 X.

---

Python 첫 번째 글자 소문자라면 무조건 스네이크 케이스.  
다음 식별자 모두 스네이크 케이스로 적힌 단어.

| print | input | list | str | map | filter |
| --- | --- | --- | --- | --- | --- |

첫 번째 글자가 대문자라면 무조건 캐멀 케이스.  
다음 식별자 모두 캐멀 케이스로 적힌 단어.

| Animal | Customer |
| --- | --- |

식별자 많은 곳에서 사용.  

---

**식별자**

- 캐멀 케이스(대문자로 시작) → **클래스**
- 스네이크 케이스(소문자로 시작)
    
    → 뒤에 괄호 O → **함수**
    
    → 뒤에 괄호 X → **변수**
    

---

캐멀 케이스 작성되 있음 **클래스**, 스네이크 케이스로 작성되어 있으면 **함수** or **변수**.  
뒤에 괄호 붙어 있으면 **함수**, 괄호 없으면 **변수**.  
약간의 예외는 존재. 대부분 경우 구분해도 문제 없음

클래스, 변수, 함수 구분하기

---

1. `print()`
2. `list()`
3. `soup.select()`
4. `math.pi`
5. `math.e`
6. `class.Animal:`
7. `beautifulSoup()`

---

1. 스네이크 케이스 뒤에 괄호 O. **함수**
2. 스네이크 케이스 뒤에 괄호 O. **함수**
3. 스네이크 케이스 뒤에 괄호 O. **함수**
4. 스네이크 케이스 뒤에 괄호 X. **변수**
5. 스네이크 케이스 뒤에 괄호 X. **변수**
6. 캐멀 케이스. **클래스**
7. 캐멀 케이스. **클래스**  
뒤에 괄호 있음. **클래스 생성자**라고 부르는 특이한 형태 함수.

# 주석

**주석(comment)** 프로그램 진행 영향 주지 않는 코드.  
프로그램 설명하기 위해 사용. Python은 다음과 같은 주석으로 처리하고자 하는 부분 앞에 # 기호 붙여 주석 처리.   
# 이후 글자 주석 처리되어 프로그램 어떠한 영향 주지 않음.

```python
>>> # 간단히 출력하는 예
>>> print("Hello World") # 문자열 출력

Hello world
```

# 연산자와 자료

**연산자**는 값과 값 사이 무언가 기능을 적용할 때 사용하는 것.  
즉, +, -와 같이 단독으로 쓰일 대 아무 의미 갖지 못함, 양쪽 숫자가 있을 대 +는 더하기, -는 빼기와 같은 기능 수행.

```python
>>> 1 + 1
2
>>> 10 - 10
0
```

자료 == **리터럴(literal)**.  쉽게 이해할 수 있는 자료 단어.   
자료란 숫자이든 문자이든 어떠한 **값** 자체를 의미. 

---

1

10

“Hello”

---

# 출력 : print()

무엇을 하는지 알 수 있도록 메시지 출력 기본 방법.  
Python 가장 기본적인 출력 방법 `print()` 함수 사용.**`print() 함수`**는 함수의 괄호 안에 출력하고 싶은 것을 나열하여 사용.

`pirnt(출력1, 출력2, . . . )`

출력1, 출력2는 하고 싶은 내용을 작성하면 된다.

## 하나만 출력

`print()` 함수 괄호 안에 출력하고 싶은 내용 작성.  
하나면 출력.

```python
>>> print("Hello World")
Hello World
>>> print(10)
10
```

## 여러 개 출력하기

`print()` 함수 뒤 출력하고 싶은 내용 쉼표로 연결해서 여러 개 작성.

숫자와 문자열 혼합, 네 개의 문자열 출력하는 예제.

```python
>>> print("Hello", "World", 10)
Hello World 10
>>> print("태희의", "Python", "TIL")
태희의 Python TIL
```

## 줄바꿈하기

`print()` 함수 괄호 안에 아무 것도 없는 경우. 아무것도 없는 경우 단순하게 **줄바꿈**하게 됨. 대화형 셸에 `print()` 입력하면 아무것도 출력하지 않고 빈 한 줄 만든 후 프롬프트 표시.

```python
>>> print()

>>> 
```

### 기본 출력

**소스 코드** | `output.py` 

# 소스 코드 | output.py

```python
# 하나만 출력
print("# 하나만 출력")
print("Hello World")
print()

# 여러개 출력
print("# 여러개 출력")
print("태희의", "Python", "TIL")
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print()

# 줄바꿈 하기
print("# 줄바꿈 하기")
print("---확인 전용선---")
print()
print()
print("---확인 전용선---")
```

Python IDLE 에디터든 VScdoe 원하는 에디터 다음과 같은 코드 입력하고 원하는 폴더 `output.py` 이름으로 저장.