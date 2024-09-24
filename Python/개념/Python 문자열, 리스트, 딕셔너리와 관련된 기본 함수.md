- 리스트에 적용할 수 있는 기본 함수
    
    `min()`, `max()`, `sum()`
    
- 리스트 뒤집기
    
    `reversed()`
    
- 현재 인덱스가 몇 번째인지 확인하기
    
    `enumerate()`
    
- 딕셔너리로 쉽게 반복문 작성하기
    
    `items()`
    
- 리스트 안에 for문 사용하기
    
    리스트 내포
    

---

# 리스트에 적용할 수 있는 기본 함수 : `min()`, `max()`, `sum()`

`min()`, `max()`, `sum()`  함수들은 리스트 매개변수로 넣어 사용 매우 기본적인 함수.

| 함수 | 설명 |
| --- | --- |
| min() | 리스트 내부에서 최솟값을 찾음 |
| max() |  리스트 내부에서 최댓값을 찾음 |
| sum() | 리스트 내부에서 값을 모두 더함 |

```python
>>> numbers = [150, 4, 9, 46, 35, 654]
>>> min(numbers)
4
>>> max(numbers)
654
>>> sum(numbers)
898
```

# `reversed()` 함수 리스트 뒤집기

리스트 요소 순서 뒤집고 싶을 때는 `reversed()` 함수 사용.  
`reversed()` 함수의 매개변수 리스트 넣으면 리스트 두집을 수 있음

### reversed() 함수

**소스 코드** | `reversed.py` 

```python
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) : ", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])) : ", list(list_reversed))
print()

print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]) : ")
for i in reversed(list_a):
	print("-", i)
```

```python
temp = reversed([1, 2, 3, 4, 5, 6])

for i in temp:
	print("첫 번째 반복문 : {}".format(i))

for i in temp:
	print("두 번째 반복문 : {}".format(i))
```

“첫 번째 부분만” 부분만 실행되고 “두 번째 반복문” 부분은 전혀 출력되지 않음

---

첫 번째 반복문 : 6

첫 번째 반복문 : 5

첫 번째 반복문 : 4

첫 번째 반복문 : 3

첫 번째 반복문 : 2

첫 번째 반복문 : 1

---

`reversed()` 함수 결과 **제너레이터이기** 때문.  
제너레이터는 Python 특별 기능. `reversed()` 함수 반복문 조합할 때 함수의 결과를 여러 번 활용하지 않고 `for` 구문 내부에 `reversed()`함수 넣어 사용.

```python
numbers = reversed([1, 2, 3, 4, 5, 6])

for i in reversed(numbers):
	print("첫 번째 반복문 : {}".format(i))

for i in reversed(numbers):
	print("두 번째 반복문 : {}".format(i))
```

# eunmerate() 함수와 반복문 조합하기

```python
example_list = ["요소A", "요소B", "요소C"]
```

---

0번째 요소는 요소A

1번째 요소는 요소B

2번째 요소는 요소C

---

### 방법(1)

```python
example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
	print("{}번째 요소 {}입니다.".format(i, item))
	i+= 1
```

### 방법(2)

```python
example_list = ["요소A", "요소B", "요소C"]
for i in range(len(example_list)):
	print("{}번째 요소 {}입니다.".format(i, example_list[i]))
```

리스트 요소 반복할 때 현재 인덱스 몇 번째인지 확인, Python은 쉽게 작성할 수 있도록 **`enumerate()` 함수** 제공

### enumerate() 함수의 리스트

**소스 코드** | `enumerate.py` 

```python
example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문 조합")
for i, value in enumerate(example_list):
	print("{}번째 요소 {}입니다.".format(i, value))
```

# 딕셔너리의 items() 함수와 반복문 조합하기

`enumerate()` 함수 반복문 조합 `for i`, `value in enumerate`(리스트) 형태 반복문 작성할 수 있던 것처럼 딕셔너리 **`items()`** 함수 함께 사용하면 키와 값 조합해서 쉽게 반복문 작성.

### 딕셔너리의 items() 함수와 반복문

**소스 코드** | `items.py` 

```python
example_dictionary = {
	"키A" : "값A",
	"키B" : "값B",
	"키C" : "값C",
}

print("# 딕셔너리 items() 함수")
print("items() : ", example_dictionary.items())
print()

print("# 딕셔너리 items() 함수와 반복문 조합")

for key, element in example_dictionary.items():
	print("dictionary[{}] = {}".format(key, element))
```

# 리스트 내포

반복문 사용 리스트 재조합하는 경우 많음.  
range(0, 20, 2)로 0부터 20사이 짝수 구한 뒤, 제곱해서 새로운 리스트 만듬

### 반복문을 사용한 리스트 생성

**소스 코드** | `for_list01.py` 

```python
array = []

for i in range(0, 20, 2):
	array.append(i * i)
print(array)
```

### 반복문을 사용한 리스트 생성

**소스 코드** | `list_in.py` 

```python
array = [i * i for i in range(0, 20, 2)]
	
print(array)
```

‘range(0, 20, 2)의 요소 i라고 할 때, i * i 로 리스트 재조합 요청’ 코드.  
구문을 **리스트 내포(list comprehensions)**라 부름

`리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]`

if 구문 넣어 조건 조합

`리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]` 

### 조건을 활용한 리스트 내포

**소스 코드** | `array_comprehensions.py` 

```python
array = ["사과", "복숭아", "젤리", "배", "체리"]
output = [fruit for fruit in array if fruit != "젤리"]

print(output)
```

‘array의 요소 `fruit`이라는 할 때 젤리이 아닌 `fruit`으로 리스트 재조합 요청’ 코드 → 젤리 제외 요소만 모인 리스트 만들어짐

‘array의 요소 `fruit`이라는 할 때 젤리이 아닌 `fruit`으로 리스트 재조합 요청’ 코드 → 젤리 제외 요소만 모인 리스트 만들어짐

## 구분 내부 여러 줄 문자열 사용했을 때 문제점

조건문과 반복문 들여쓰기.  
구문 내부 여러 줄의 문자열 만들면 예상치 못한 실행 결과 발생

### if 조건문과 여러 줄 문자열(1)

**소스 코드** | `if_string.py` 

```python
number = int(input("정수 입력> "))

if number % 2 == 0:
	print("""\
		입력한 문자열은 {}입니다.
		{}는(은) 짝수입니다.""".format(number, number))

else:
	print("""\
		입력한 문자열은 {}입니다.
		{}는(은) 홀수입니다.""".format(number, number))
```

프로그램 실행하면 여러 줄 문자열 앞 들여쓰기가 문자열 포함되어 들어가는 것을 볼 수 있음. → 예상치 못한 들여쓰기 막기

### if 조건문과 여러 줄 문자열(2)

**소스 코드** | `if_string01.py` 

```python
number = int(input("정수 입력> "))

if number % 2 == 0:
	print("""입력할 문자열은 {} 입니다.
	{}는(은) 짝수입니다.""".format(number, number))
	
else:
	print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))
```

여러 줄 문자열을 if 조건문, for 반복문, while 반복문 등의 구문과 함께 사용하면 이런 문제가 발생.  
→ 구문 내부에서는 여러 줄 문자열을 거의 사용하지 않는 편. → 문자열을 한줄로 길게 적으면 코드가 복잡해진다.

### if 조건문과 긴 문자열

**소스 코드** | `if_string02.py` 

```html
number = int(input("정수 입력> "))

if number % 2 == 0:
	print("입력한 문자열은 {}입니다.\n는(은) 짝수".format(number, number))
else:
	print("입력한 문자열은 {}입니다.\n는(은) 홀수".format(nubmer, number))
```

여러 줄 문자열과 구문 함께 사용할 때 발생하는 문제 해결 방법 많음

## 괄호로 문자열 연결하기

Python 문자열 생성할 때 구문. 괄호 내부 문자열 여러개 입력 모든 문자열 합친 새로운 문자열 만들어짐.

### 괄호로 문자열 연결하기

**소스 코드** | `string01.py` 

```python
test = (
    "아니"
    "근데"
    "진짜 한 줄?"
)

print("test:", test)
print("type(test):", type(test))
```

코드 실행 → 변수 test 자료형 문자열 자료형이라는 것 알 수 있음

### 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)

**소스 코드** | `string02.py` 

```python
number = int(input("정수 입력> "))

if number % 2 == 0:
	print(
		"입력한 문자열 {}.\n"
		"{}는(은) 짝수.").format(number, number)
else:
	print((
		"입력한 문자열 {}.\n"
		"{}는(은) 홀수.").format(number, number))
```

## 문자열의 `join()` 함수

문자열 `join()` 함수.

`문자열.join(문자열로 구성된 리스트)`

**`join()`** 함수는 리스트 요소 문자열로 연결

```python
>>> print("::".join(["1", "2", "3", "4", "5"]))
1::2::3::4::5
```

여러 줄 문자열과 if 구문 조합했을 때 문제 해결.

### 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(2)

**소스 코드** | `string03.py` 

```python
number = int(input("정수 입력> "))

if number % 2 == 0:
	print("\n".join([
		"입력한 문자열 {}."
		"{}는(은) 짝수,"
	]).format(number, number))
else:
	print("\n".join([
		"입력한 문자열 {}."
		"{}는(은) 홀수,"
	]).format(number, number))
```

# 이터레이터

반복문 구문.

`for 반복자 in 반복할 수 있는 것`

‘반복할 수 있는 것’ 프로그래밍 용어로 **이터러블(iterable).** 이터러블은 내부 있는 요소 차례차례 꺼낼 수 있는 객체 의미. 리스트, 딕셔너리, 문자열, 튜플 등 모두 내부 요소 차례차례 꺼낼 수 있으므로 이터러블.

이터러블 중 **`next()`** 함수 적용 하나하나 꺼낼 수 있는 요소 **이터레이터(iterator)**

### reversed() 함수와 이터레이터

**소스 코드** | `lterator01.py` 

```python
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_numbers : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
```

`reversed()` 함수 사용 `<list_reverseiterator object at (주소)>`처럼 출력 `reversed()` 함수 리턴값 → **reverseiterator**로 **이터레이터**.  
이터레이터는 반복문 매개변수 전달, 코드처럼 `next()` 함수 내부 요소 하나하나 꺼낼 수 있음

`for` 반복문 매개변수 넣으면 반복할 때마다 `next()` 함수 사용 요소 하나하나 꺼내주는 것.  

why? | `reversed()` 함수 리스트 바로 리턴해 주지 않고 이터레이터를 리턴함. → 메모리의 효율성 위함. 1만 개 요소 들어 있는 리스트 복제한 뒤 리턴하는 것보다 기존 있던 리스트 활용 작업하는 것이 훨씬 효율적이라 판단