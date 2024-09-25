# 튜플

튜플은 리스트와 비슷한 자료.  
리스트와 다른 점은 한번 결정된 요소 바꿀 수 없다는 것. 일반적으로 튜플은 함수 많이 사용하면 다음과 가은 형태로 생성

`(데이터, 데이터, 데이터, . . .)`

튜플 생성한 후 각 요소 출력

```python
>>> tuple_test = (10, 20, 30)
>>> tuple_test[0]
10
>>> tuple_test[1]
20
>>> tuple_test[2]
30
```

튜플과 리스트 차이 없음.  
요소 변경할 때 차이가 있음. 0번째 요소 1을 넣으려고 하니 오류 발생. 튜플은 내부 요소 변경 불가능하기 때문.

```python
>>> tuple_test[0] = 1
Traceback (most recent call last):
	File "<pyshell#1>", line 1, in <module>
		tuple_test[0] = 1
TypeError: 'tuple' object does not support item assignment
```

튜플은 형태만 보면 리스트와 너무 동일하여 리스트만 사용, 왜 튜플을 사용할까? 튜플은 언제 유용할까?

## 괄호 없는 튜플

Python 리스트와 튜플은 특이한 형태 할당 구문 사용.  

### 리스트와 튜플의 특이한 사용

**소스 코드** | `tuple_basic.py` 

```python
# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a : ", a)
print("b : ", b)
print("c : ", c)
print("d : ", d)
```

리스트와 튜플 사용 같은 형태 변수를 선언하고 할당.  
튜플의 특이한 성질. 괄호를 생략해도 튜플로 인식할 수 있는 경우는 괄호를 생략해도 됨.

### 괄호가 없는 튜플

**소스 코드** | `tuple_use01.py` 

```python
# 괄호 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호 없는 튜플의 값과 자료형 출력")
print("tuple_test : ", tuple_test)
print("type(tuple_test) : ", type(tuple_test))
print()

# 괄호 없는 튜플 활용
a, b, c = 10, 20, 30
print("# 괄호 없는 튜플 활용한 할당")
print("a : ", a)
print("b : ", b)
print("c : ", c)
```

괄호 없이 여러 값 할당할 수 있어 자주 사용되는 형태.   
특이한 구문 편리함은 다음 코드 확인. 변수의 값을 교환하는 코드

### 변수의 값을 교환하는 튜플

**소스 코드** | `tuple_use02.py` 

```python
a, b = 10, 20

print("# 교환 전 값")
print("a : ", a)
print("b : ", b)
print()

# 값 교환
a, b = b, a

print("교환 후 값")
print("a : ", a)
print("b : ", b)
print()
```

a, b = b, a라는 코드만으로 값이 바뀜.  
편리하게 사용할 수 있는 값 교환 방법이므로 알아두기.

## 튜플과 함수

튜플은 함수의 리턴에 많이 사용.  
함수의 리턴에 튜플을 사용하면 여러 개의 값 리턴하고 할당할 수 있음.

### 괄호가 없는 튜플

**소스 코드** | `tuple_return.py` 

```python
# 함수 선언
def test():
	return (10, 20)

# 여러 개 값 리턴
a, b = test()

print("a : ", a)
print("b : ", b)
```

# 람다

프로그래밍 언어 함수라는 ‘기능’을 매개변수 전다라하는 코드 많이 사용.  
코드를 조금 더 효율적으로 작성할 수 있도록 Python **람다(lambda)** 기능 제공

## 함수의 매개변수로 함수 전달하기

함수의 매개변수로 함수를 전달하는 코드.  
함수의 매개변수에 상요하는 함수를 **콜백 함수(callback function)**

### 함수의 매개변수로 함수 전달하기

**소스 코드** | `func_as_param.py` 

```python
# 매개변수로 받은 함수 10번 호출하는 함수
def call_10_times(func):
	for i in range(10):
		func()

# 간단한 출력하는 함수
def print_hello():
	print("Hello")

# 조합
call_10_times(print_hello)
```

프로그램 실행 `print_hello()` 함수 10번 실행.  
”Hello”라는 문자열 10번 출력

## `filter()` 함수와 `map()` 함수

함수를 매개변수로 사용하는 대표적인 **표준 함수**로 `map()` 함수와 `filter()`함수.

---

note | Python 표준으로 제공하는 함수 ‘내장 함수’ 똔느 ‘표준 함수’라 부름

---

**`map()`** 함수는 리스트 요소를 함수에 넣고 리턴된 값 새로운 리스트를 구성해 주는 함수.

`map(함수, 리스트)`

**`filter()`** 함수는 리스트의 요소를 함수에 넣고 리턴된 값 Ture 인 것으로, 새로운 리스트 구성해 주는 함수.

`filter(함수, 리스트)`

### map() 함수와 filter() 함수

**소스 코드** | `call_with_func.py` 

```python
# 함수 선언
def power(item):
	return item * item
def under_3(item):
	return item < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", output_b)
```

`map()` 함수와`filter()` 함수는 모두 첫 번째 매개변수 함수, 두 번째 매개변수에 리스트 넣음. 일단 `map()` 함수.  
첫 번째 매개변수에 값을 제곱해주는 `power()` 함수 넣음

두 번 째 매개변수에는 [1, 2, 3, 4, 5]라는 리스트 넣음.  
결과 [1, 2, 3, 4, 5] 내부의 요소 `pwoer()` 함수 적용된 [1, 4, 9, 16, 25] 얻음

`filter()` 함수.  
첫 번째 매개변수에는 `item < 3을 판정하는 under_3()` 함수를 넣음. 두 번째 매개변수에는 [1, 2, 3, 4, 5]라는 리스트 넣음.  
결과 [1, 2, 3, 4, 5] 내부 요소 중 `item < 3 True인 [1, 2]` 얻음

결과. `<map object>`와 `<filer object>`가 나옴, 이를 **제너레이터(generator)**. `list()` 함수 적용 강제로 리스트 자료형으로 변환해 출력. 처음 보면 조금 당황할 수 있는 두 함수. 

## 람다의 개념

매개변수로 함수 전달하기 위해 함수 구문 작성하는 것 번거롭고, 코드 공간 낭비라는 생각 들 수 있음. 그래서 만들어진 개념 **람다(lambda).**

람다는 ‘간단한 함수를 쉽게 선언하는 방법’.

`lambda 매개변수 : 리턴값`

코드 람다로 변경해 봄. power() 함수와 under_3() 함수를 람다로 변환. def 키워드 선언했던 함수 lambda 바꾸고, return 키워드 따로 쓰지 않았다는 정도 차이 생김

### 람다

**소스 코드** | `lambda01.py` 

```python
# 함수 선언
power = lambda x : x * x
under_3 = lambda x : x * x

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수 실행 결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수 실행 결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))
```

람다는 간단한 함수를 쉽게 선언하는 방법, 사용하는지 의심스러울 정도로 복잡한 코드

람다는 함수의 매개변수에 곧바로 넣을 수 있음

### 인라인 람다

**소스 코드** | `lambda02.py` 

```python
# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map () 함수 사용
output_a = map(lambda x : x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(lambda x : x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))
```

람다를 사용하면 코드 더 깔끔하게 작성, 함수가 매개변수 넣어졌다고 확인 어떤 함수인지를 알기 위해 다시 찾아 올라가는 수고 하지 않아도 됨

함수가 매개변수로 넣어졌다고 확인 어떤 함수인지 알기 위해 다시 찾아 올라가는 수고 하지 않아도 됨

# 파일 처리

Python 표준 함수 파일과 관련된 처리 하는 함수 기본 제공.  
파일은 크게 **텍스트 파일**과 **바이너리 파일**로 나뉘는데, 여기서는 ‘텍스트 파일’과 관련된 내용만 살펴보기.

파일 처리하려면 일단 **파일 열기(open)**. 파일을 열면 **파일 읽기(read)** 또는 **파일 쓰기(write).**

## 파일 열고 닫기

파일 열 때는 **`open()`** 함수 사용.

`파일 객체 = open(문자열 : 파일 경로, 문자열 : 읽기 모드)` 

open() 함수 첫 번째 매개변수에는 파일 경로(path) 입력, 두 번째 매개변수에는 모드(mode)를 지정. 

모드 저장.

| 모드 | 설명 |
| --- | --- |
| w | write 모드 (새로 쓰기 모드) |
| a | append 모드 (뒤에 이어서 쓰기 모드) |
| r | read 모드 (읽기 모드) |

파일 닫을 때 **`close()`** 함수 사용

`파일 객체.close()`

### 파일 열고 닫기

**소스 코드** | `file_open.py` 

```python
# 파일 열기
file = open("basic.txt", "w")

# 파일에 텍스트를 쏩
file.write("Hello World Python")

# 파일 닫기
file.close()
```

프로그램 실행 시 폴더에 basic.txt 라는 파일 생성

파일을 메모장 등으로 열어 보면 `file_open.py`에 입력한 글자 출력 되어 있음

`open()` 함수 파일 열면 `close()` 함수로 파일을 닫아 주어야 함. 프로그램 종료될 때 열려있는 파일 모두 자동으로 닫고 종료. 그렇다고 `close()` 함수 따로 사용하지 않아도 된다고 생각하면 안됨. 반드시 `open()` 함수 열면 `close()` 함수로 닫는 습관.

## with 키워드

프로그램 길어지면 `open()` 함수와 `close()` 함수 사이 많은 코드 들어감. 조건문과 반복문이 들어가다 보면 파일 열고 닫지 않는 실수 하는 경우 생길 수 있음. 실수 방지하기 위해 **with 키워드**라는 기능 있음.  

with 키워드 구문

---

with open(문자열 : 파일 경로, 문자열 : 모드) as 파일 객체:

문장

---

```python
# 파일 열음
with open("basic.txt", "w") as file:
	# 파일 텍스트
	file.write("Hello World Python")
```

코드 작성하면 with 구문 종료될 때 자동으로 파일 닫힘.  
따라서 파일 열고 닫지 않는 실수 줄임

## 텍스트 읽기

파일 텍스트 쓸 때 **`write()`** 함수 사용.  
반대로 파일을 읽을 때는 **`read()`** 함수 사용

`파일 객체.read()`

파일 열고 파일 객체 `read()` 함수 호출하기만 하면 내부 있는 데이터 모두 읽어 출력.

### read() 함수로 텍스트 읽기

**소스 코드** | `file_read.py` 

```python
# 파일 열기
with open("basic.txt", "r") as file:
	# 파일 읽고 출력
	contents = file.read()
print(contents)
```

## 텍스트 한 줄씩 읽기

텍스트 사용 데이터 구조적 표현할 수 있는 방법 **CSV, XML, JSON** 등 있음. 이 중 CSV는 Comma Separated Values의 줄임말, 쉼표 구분된 값들을 의미. 데이터 CSV 형식 대표적인 예

---

이름, 키, 몸무게 → 헤더

홍길동, 180, 70 → 데이터

---

CSV 파일 한 줄에 하나의 데이터, 각각의 줄 쉼표를 사용해 데이터 구분.  이때 첫 번째 줄에 헤더(header) 넣어 각 데이터 뭉서 나타내는지 설명

CSV 라는 용어 그냥 ‘홍길은 키 180 몸무게 70’로 이해.

도마 위 야채 올려놓고 자를 때 한 번에 모든 재료를 올려놓고 자르지 않는다. 한 번  자를 수 있는 만큼 자르고 처리하는 것 반복. 데이터 처리 할 때도 마찬가지. 한 번 데이터 모두 읽어 들이기보다는 ‘한 번에 한 명씩’ 처리하는 경우 많음.

### 랜덤하게 1000명의 키와 몸무게 만들기

**소스 코드** | `file_write.py` 

```python
# 랜덤한 숫자 만들기 위해 가져옴
import random
# 간단한 한글 리스트
hanguls = list("가나다라마바사아자차카타파하")
# 파일 쓰기 모드
with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 씀
        file.write("{}, {}, {}\n".format(name, weight, height))

```

데이터 많이 있다고 가정하고 한 줄씩.   
데이터를 한 줄씩 읽어 들일 때는 **for 반복문**을 다음과 같은 형태로 사용.

---

for 한 줄을 나타내는 문자열 in 파일 객체:

처리

---

### 반복문으로 파일 한 줄씩 읽기

**소스 코드** | `file_readlines.py` 

```python
with open("info.txt", "r") as file:
	for line in file:
		# 변수 선언
		(name, weight, height) = line.strip().split(", ")
		
		# 데이터 문제없는지 확인 : 문제 있으면 지나감
		if (not name) or (not weight) or (not height):
			continue
		# 결과 계산
		bmi = int(weight) / ((int(height) / 100) ** 2)
		result = ""
		if 25 <= bmi:
			result = "과체중"
		elif 185 <= bmi:
			result = "정상 체중"
		else:
			result = "저체중"
		
		# 출력
		print('\n'.join([
			"이름 : {}",
			"몸무게 : {}",
			"키 : {}",
			"BMI : {}",
			"결과 : {}"
		]).format(name, weight, height, bmi, result))
		print()
```

# 혼자 공부하는 Python 프로그래밍

- **공식 문서 또는 튜트리얼 사이트**
    
    함수 등 검색했을 때 함수들의 사용법 나오는 튜트리얼(사용 지침서) 사이트. 확인하면서 함수의 기본적인 사용 방법 기술된 페이지 방문
    
- **스택 오버플로우**
    
    프로그래밍의 다양한 주제에 대한 질문 답변 사이트, 특정한 함수 사용할 때 문제 발생한 사람들의 질문들도 올라옴. 함수 사용할 때의 중의점, 활용하는 방법 살펴볼 수 있음.
    

# 제너레이터

**제너레이터(generator)** Python 특수한 문법 구조.   
제너레이터는 **이터레이터** 직접 만들 때 사용하는 코드. 함수 내부 **yield 키워드** 사용하면 해당 함수 제너레이터 함수 되며, 일반 함수와는 달리 함수 호출해도 함수 내부의 코드 실행되지 않음.

### 제너레이터 함수

**소스 코드** | `generator.py` 

```python
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
```

test() 함수 호출 “함수 호출”. 문자열 출력되어야 하지만, 출력되지 않았음. 함수의 리턴값으로 <generator object test at 0x02F20C90> 등 출력. 즉 제너레이터 함수는 제너레이터 리턴. 출력된 <generator object test at 0x02F20C90>는 제너레이터 객체

제너레이터 객체는 **`next()`** 함수 사용해 함수 내부 코드 실행.  
이 때 yield 키워드 부분까지만 실행, next() 함수 리턴값으로 yield 키워드 뒤 입력한 값 출력.

### 제너레이터 객체와 next() 함수

**소스 코드** | `generator01.py` 

```python
# 함수 선언
def test():
	print("A 지점 통과")
	yield 1
	print("B 지점 통과")
	yield 2
	print("C 지점 통과")

# 함수 호출
output = test()
# next() 함수 호출
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)
# 한 번 더 실행
next(output)
```

코드 실행 next() 함수 호출 “A 지점 통과”, “B 지점 통과”, “C 지점 통과”처럼 함수 내부 내용 진행되는 모습 확인. next() 함수 호출한 이후 yield 키워드 만나지 못하고 함수 끝나면 **Stoplteration** 이라는 예외 발생

제너레이터 객체는 함수의 코드 조금씩 실행할 때 사용.  
메모리의 효율성 위해서 제너레이터 객체와 이터레이터 객체는 완전히 같지는 않지만, 기본적인 단계에서는 거의 비슷하다 봐도 무방.

# 리스트 함수의 key 키워드 매개변수

리스트 최솟값과 최댓값 찾을 때 **`min()`** 함수와 **`max()`** 함수 사용

```python
>>> a = [100, 51 ,98, 32 ,5]
>>> min(a)
5
>>> max(a)
100
```

‘가격이 가장 저렴한 책’과 ‘가격이 가장 비싼 책’ 찾고 싶을때는?

딕셔너리에 있는 **키** 활용.  
`min()` 함수와 `max()` 함수에는 ‘어떤 값으로 비교’할 것인지 나타내는 key라는 키워드 매개변수 지정. 활용하면 딕셔너리 있는 가격 속성으로 최댓값과 최솟값을 비교

### 키워드 매개변수에 함수 전달하기

**소스 코드** | `func_as_keyparam.py` 

```python
books = [{
	"제목" : "혼자 공부하는 Python",
	"가격" : 18000
}, {
	"제목" : "혼자 공부하는 머신러닝 + 딥러닝",
	"가격" : 26000
}, {
	"제목" : "혼자 공부하는 Java",
	"가격" : 24000
}]

def 가격추출함수(book):
	return book["가격"]
	
print("# 가장 저렴한 책")
print(min(books, key=가격추출함수))
print()

print("# 가장 비싼 책")
print(max(books, key=가격추출함수))
```

람다로 수정한다면 코드를 어떻게 바꿔야할까?

### 콜백 함수를 람다로 바꾸기

**소스 코드** | `lambda03.py` 

```python
books = [{
	"제목" : "혼자 공부하는 Python",
	"가격" : 18000
}, {
	"제목" : "혼자 공부하는 머신러닝 + 딥러닝",
	"가격" : 26000
}, {
	"제목" : "혼자 공부하는 Java",
	"가격" : 24000
}]

def 가격추출함수(book):
	return book["가격"]
	
print("# 가장 저렴한 책")
print(min(books, key=lambda book: book["가격"]))
print()

print("# 가장 비싼 책")
print(max(books, key=lambda book: book["가격"]))
```

리스트 요소 정렬할 때 sort() 함수 사용 했음. sort() 함수는 파괴적 함수이므로 호출했을 때 리스트 자체 바뀜.

```python
# sort 함수로 오름차순 정렬하기
>>> a = [100, 51 ,98, 32 ,5]
>>> a.sort()
>>> a
[5, 32, 51, 98, 100]
```

기본 오름차순 정렬 만약 내림차순 정렬하고 싶다면 reverse 키워드 매개변수 True 지정

```python
>>> a.sort(reverse=True)
>>> a
[100, 98, 51, 32, 5]
```

단순한 숫자 리스트 아니라 ‘딕셔너리의 리스트’처럼 복합적인 리스트 정렬할 때는 어떻게 할까? 이럴 때도 딕셔너리의 키를 활용 **key 키워드 매개변수**에 **람다** 사용.

### 딕셔너리 오름차순 정렬하기

**소스 코드** | `lambda04.py` 

```python
books = [{
	"제목" : "혼자 공부하는 Python",
	"가격" : 18000
}, {
	"제목" : "혼자 공부하는 머신러닝 + 딥러닝",
	"가격" : 26000
}, {
	"제목" : "혼자 공부하는 Java",
	"가격" : 24000
}]

def 가격추출함수(book):
	return book["가격"]
	
print("# 가장 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
	print(book)
```

# 스택, 힙

Python 기본 자료형 숫자, 문자열, 불 있음.  
이 세 가지 제외한 자료형들 모두 **객체 자료형**.  기본자료형과 객체 자료형의 차이점.

**기본 자료형**은 가볍고 정형화된 자료형. Python 작은 상자 기본 자료형 저장하며 이를 쌓아서 모아둔다. 이렇게 기본 자료형 차곡차곡 정리되어 있는 공간 **스택(stack).**

```python
a = 10
b = True
c = "Hello"
```

**객체 자료형**은 무겁고 크기가 정형화되어 있지 않음. 스택처럼 차곡차곡 쌓아 정리할 수 없으므로 Python 이를 거대한 창고 넣어둠. 객체 자료형 저장되어 있는 거대한 창고를 **힙(heap)**이라고 함.

```python
d = [1, 2, 3, 4, 5]
e = {"이름" : "구름", "나이 : 6"}
```

스택 있는 자료 잘 정리되어 있어 수비고 빠르게 찾을 수 있지만, 힙 있는 자료는 힙이라는 창고 너무 크기 때문에 쉽게 찾을 수 없음 Python 특별한 방법 사용

**리스트**와 **딕셔너리** 같이 큰 자료형 힙이라는 창고 넣어두고 창고 어떤 위치 저장했는지 **스택**에 기록.

창고 위치한 선반 컴퓨터 과학에서는 **16진수 숫자**로 표현.

창고 어떤 위치 저장했는지 **주소(address)** 또느 **래퍼런스(reference)**라고 부름.