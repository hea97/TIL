# 불 만들기 : 비교 연산자

불은 비교연산자 통해 만들 수 있음. Python 여섯 개의 비교 연산자 존재 

| 연산자 | 설명 | 연산자 | 설명 |
| --- | --- | --- | --- |
| == | 같다 | > | 크다 |
| ≠ | 다르다 | ≤ | 작거나 크다 |
| < | 작다 | ≥ | 크거나 같다 |

```python
>>> print(10 == 100)
False
>>> print(10 != 100)
True
>>> print(10 < 100)
True
>>> print(10 > 100)
False
>>> print(10 <= 100)
True
>>> print(10 >= 100)
False
```

| 조건식 | 의미 | 결과 |
| --- | --- | --- |
| 10 == 100 | 10이 100과 같은가 | False |
| 10 != 100 | 10이 100과 다른가 | True |
| 10 < 100 | 10이 100보다 작은가 | True |
| 10 > 100 | 10이 100보다 큰가 | False |
| 10 <= 100 | 10이 100보다 작거나 같은가 | True |
| 10 >= 100 | 10이 100보다 크거나 같은가 | False |

Python 문자열 비교 연산자 적용. 한글은 사전 순서(가나다순)로 앞 있는 것이 작은 값 갖음.  
e.g. ‘가방’과 ‘하마’ 비교 사전 순서 ‘가방’ 앞 있음 ‘가방’이 ‘하마’보다 작은 값 갖음.

```python
>>> print("가방" == "가방")
True
>>> print("가방" != "하마")
True
>>> print("가방" < "하마")
True
>>> print("가방" > "하마")
False
```

# 불 연산하기 : 논리 연산자

불 만들 때 비교 연산자 사용.  
불끼리 논리 연산자 사용 Python의 3가지 논리 연산자

| 연산자 | 의미 | 설명 |
| --- | --- | --- |
| not | 아니다 | 불을 반대로 전환 |
| and | 그리고 | 피연산자 두 개 모두 참일 때 True 출력, 그 외 모두 False 출력 |
| or | 또는  | 피연산자 두 개 중에 하나만 참이라도 True 출력, 두 개 모두 거짓일 때만 False 출력 |

## not 연산자

**not 연산자**는 **단항 연산자**, 참과 거짓 반대로 바꿀 때 사용.  
단순하게 True와 False가 서로 바뀜

```python
>>> print(not True)
False
>>> print(not False)
True
```

True와 False 바로 not 연산자 적용 경우 없음.  
일반적으로 비교 연산자 불 자료형 변수, not 연산자 적용

### not 연산자 조합하기

**소스 코드** | `boolean.py` 

```python
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20:", not under_20)
```

## and 연산자 or 연산자

not 연산자는 대부분 쉽게 이해, and 연산자 or 연산자는 조금 이해하기 힘듬.  

**and 연산자**는 양쪽 변의 값 모두 참일 때 True 결과 나타냄

| 좌변 | 우변 | 결과 |
| --- | --- | --- |
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | Falsec |

**or 연산자** 둘 중 하나 참이어도 True 결과 나타냄

| 좌변 | 우변 | 결과 |
| --- | --- | --- |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | Falsec |

“사과 **그리고** 배 가져와” → 의미는 두 가지를 모두 가지고 오라는 의미.

“사과 **또는** 배 가져와” → 둘 중 하나라도 가지고 오라는 의미.

프로그래밍에서도 비슷하게 좋은 것은 True 좋지않은 것은 False라고 가정했을 때

명령 수행하면 True, 수행하지 못하면 False라 가정.

“치킨(True) **그리고** 쓰레기(False) 가져와” → 둘 다 오라는 명령, 쓰레기 가져가기 싫음 → 명령 거부 False.

“치킨(True) **또는** 쓰레기(False) 가져와” → 둘 중 하나만 들 가면 되니까 치킨만 가져감. → True.

```python
>>> print(True and True)
True
>>> print(True and False)
False
>>> print(True and True)
False
>>> print(True and False)
False
>>> print(True or True)
True
>>> print(True or False)
True
>>> print(True or True)
True
>>> print(True or False)
False
```

# 논리 연산자의 활용

## and 연산자

and 연산자 사용하는 경우.  
어떤한 공연 티켓을 예매할 경우 ‘티켓을 1장만 구매하면서 오후 3시 이후’라는 조건 나타남

---

티켓 1장 이하 **AND** 오후 3시 이후 = 티켓 구매 가능

---

두 가지 조건 모두 충족할 때만 티켓 구매 가능 **and(그리고) 연산자**도 같은 방식

## or 연산자

or 연산자 사용 경우.  
’결제한 카드 XX카드나 OO카드라면 10% 할인’이라는 조건

---

XX카드 **OR** OO카드 = D.C 10%

---

논리 연산자 다양한 곳에서 활용됨.

# if 조건문

Python if 조건문 조건 따라 코드 실행 or 실행하지 않게 만들고 싶을 때 사용하는 구문.   
코드의 실행 흐름 변경한다는 뜻. 조건을 기반으로 실행의 흐름을 변경하는 것을 **조건 분기**라 부름.    

---

if 불 값이 나오는 표현식: → if 조건은 뒤에 반드시 콜론(:) 붙여야 함.

    불 값이 참일 때 실행 문장

    불 값이 참일 때 실행 문장

→ if문은 4칸 들여쓰기 후 입력. (들여쓰기 X == 오류 발생)

---

조건문 기본적 형태 간단한 예제.  
if 뒤 불 값이 참 들여쓰기된 명령문을 실행하여 “True”와 “정말 True“

```python
>>> if True:
	    print("True")
	    print("정말 True")
```

if 뒤에 있는 불 값 거짓 경우 들여쓰기 된 명령문 있다고 하더라도 아무것도 실행 X.

```python
>>> if False:
	    print("False")
	    
```

---

**note** | 인터렉티브 셸에서 if 조건문 입력 |Enter| 키 누르면 다음 줄 프롬프트 위치에 . . . 나타남. → 코드 입력 끝나지 않음을 자동으로 알려주는 표시. 이 위치부터 4칸 들여쓰기 후 실행 문장 입력.

---

### 조건문의 기본 사용

**소스 코드** | `condition.py` 

if문 사용 양수 입력 “양수”. 음수 입력 “음수”. 0을 입력하면 “0”을 출력하는 예시

```python
# 입력
number = input("정수 입력>")
number = int(number)

# 양수 조건
if number > 0:
	    print("양수")
	    
# 음수 조건
if number < 0:
	    print("음수")
	    
# 0 조건
if number == 0:
	    print("0")
```

# 날짜/시간 활용하기

### 날짜/시간 출력하기

**소스 코드** | `date.py` 

시간 조건으로 구분하여 오전/오후 인지 출력하는 프로그램 작성.  
Python에서는 코드를 `import **datetime`** 와 `now = **datetime.datetime.now()`**  코드 사용하면 날짜, 시간 구분. 

```python
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
```

**모듈**이라는 기능 활용 **`datetime`**이라는 기능 가져오는게 첫번째.  
**`datetime.datetime.now()`** 함수 현재 시간을 구해 now라는 변수에 대입.  
마지막으로 `now.year(년)` , `now.month(월)` , `now.day(일)` , `now.hour(시)` , `now.minute(분)`, `now.second(초)`  사용해 현재의 년, 월, 일, 시, 분, 초 출력

### 날짜/시간을 한 줄로 출력하기

**소스 코드** | `date01.py` 

`format()` 함수 활용 날짜 한누에 볼 수 있게 출력

```python
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
			now.year, now.month, now.day, 
			now.hour, now.minute, now.second))
```

### 오전과 오후를 구분하는 프로그램

**소스 코드** | `date02.py` 

```python
# 날짜/시간 관련된 기능 가져옴
import datetime

# 현재 날짜/시간 구함
now = datetime.datetime.now()

if now.hour < 12:
	    print("현재 시각은 {}시로 오전.".format(now.hour))
if now.hour >= 12:
	    print("현재 시각은 {}시로 오후.".format(now.hour))
```

현재 시각은 오후 7시.  
만약 새벽 3시에 프로그램 실행학먄 “현재 시각은 3시 오전” 출력

### 계절을 구분하는 프로그램

**소스 코드** | `date03.py` 

```python
# 날짜/시간과 관련된 기능
import datetime

now = datetime.datetime.now()

# 계절
if 3 <= now.month <= 5:
	    print("이번 달은 {}월로 봄".format(now.month))
if 6 <= now.month <= 8:
	    print("이번 달은 {}월로 여름".format(now.month))
if 9 <= now.month <= 11:
	    print("이번 달은 {}월로 가을".format(now.month))
if now.month == 12 or 1 <= now.month <= 2:
	    print("이번 달은 {}월로 겨울".format(now.month))
```

봄 3월 ~ 5월 3보다 크거나 같고 5보다 보다 작거나 같은지 묻는 조건식

`3 <= now.month <= 5` 

그리고 여름, 가을도 마찬가지

겨울의 경우는 12월과 1, 2월으므로 or 연산자 사용 범위 연결.

# 짝수와 홀수 구분하기 (누적 예제)

### 끝자리로 짝수와 홀수 구분

**소스 코드** | `condition01.py` 

---

if 불 값이 나오는 표현식:    

    불 값이 참일 때 실행할 문장

---

구문 자체 매우 간단.  

```python
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
```

52라고 입력하였을 때, “짝” 출력.

### in 문자열 연산자를 활용해서 짝수와 홀수 구분

**소스 코드** | `condition02.py` 

```python
number = input("정수 입력> ")
last_character = number[-1]

if last_character in "02468":
	    print("짝")
if last_character in "13579":
	    print("홀")
```

`last_character`  문자열 “02468” 이라는 문자열 포함되어 있는지 혹은 “13579”라는 문자열 포함되어 있는지 학인해 홀 혹은 짝 출력 하는 코드가 조금 더 깔끔해짐

### 나머지 연산자를 활용해서 짝수와 홀수 구분

**소스 코드** | `condition03.py` 

```python
nubmer = input("정수 입력> ")
nubmer = int(nubmer)

if nubmer % 2 == 0:
	    print("짝")
if nubmer % 2 == 1:
	    print("헐")
```

단순하게 2로 나눈 나머지가 0이면 ‘짝’, 1이면 ‘홀’이라고 지정.  
우리는 짝수와 홀 구분 할 때 끝자리를 보지만, 컴퓨터는 2로 나눈 나머지가 0인지 확인 시키는 것이 좋음 → 그래애 컴퓨터가 더 빨라짐