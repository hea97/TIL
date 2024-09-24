# 문자열의 `format()` 함수

`format()` 함수로 숫자 문자열 변환하는 몇 가지 형태 살펴보기

**`format()`** 함수는 문자열 가지고 있는 함수.  
중괄호{}를 포함한 문자열 뒤 마침표(.) 찍고 `format()` 함수 사용, 중괄호 개수와 format 함수 괄호 안 매개변수 개수 반드시 같아야 함.

---

`“{ }”. format(10)`

`“{ } { }”. format(10, 20)`

`“{ } { } { } { } { }”.format(101, 202, 303, 404, 505)`

---

형태로 함수 사용하면 앞쪽 있는 문자열 {} 기호 `format()` 함수 괄호 안에 있는 매개 변수 차례로 대치되면서 숫자 문자열 되는 것.

### `format()` 함수로 숫자를 문자열로 변환하기

**소스 코드** | `format_basic.py` 

```python
# format() 함수 숫자를 문자열 변환
string_a = "{}".format(10)

# 출력
print(string_a)
print(type(string_a))
```

10의 자료형은 문자열, string_a에는 문자열 10이 들어있음

format이라는 함수는 {} 기호 format 괄호 안에 있는 매개변수 대체하는 것 뿐이기 떄문에 {} 기호 앞 뒤 혹은{} 기호와 {} 기호 사이에 다양한 문자열 넣을 수 있음

### `format()` 함수의 다양한 형태

**소스 코드** | `format01.py` 

```python
# format() 함수 숫자를 문자열로 변환
format_a = "{}만 원".format(5000)
format_b = "Python 중고가 {}원".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력
print(format_a)
print(format_b)
print(format_c)
print(format_d)
```

`format_a`는 {} 기호 옆 다른 문자열 넣은 형태.   
{}라는 기호 부분만 `format()` 함수 매개변수 넣은 5000으로 대치

`format_b`는 {} 기호의 앞뒤로 다른 문자열 넣은 형태.    
foramt() 함수의 매개변수 넣은 5000이 대치되어 표현 방법 달라짐

`format_c`는 매개변수를 여러 개 넣은 형태.  
입력하면 차례대로 해당 위치 맞게 대치

`format_d`는 ‘숫자를 문자열로 변환’과는 관련 X.  
`format()` 함수는 숫자 이외 자료형에도 적용할 수 있다는 예.

# `format()` 함수의 다양한 기능

format() 함수는 숫자와 관련해서도 다양한 기능 가지고 있음

## 정수 출력의 다양한 형태

`format()` 함수 사용하면 출력할 정수에 기호 넣기, 숫자 형태를 다야하게 출력.

### 정수를 특정 칸에 출력하기

**소스 코드** | `format02.py` 

```python
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
```

output_a는 {:d}를 사용. int 자료형 정수를 출력하겠다고 직접적으로 지정하는 것. 따라서 {:d}를 사용했을 때는 매개변수로 정수만 올 수 있음.

output_b와 output_c는 특정 칸 맞춰 숫자 출력하는 형태.  
{:5d}라고 입력 하면 5칸 빈 칸으로 잡고 뒤에 10라는 숫자 채움. {:10d}도 마찬가지로 10칸 빈 칸 잡고 뒤에 10라는 숫자 채움.

output_d와 output_e는 빈칸 0으로 채우는 형태.  
{:05d}라고 지정하면 5칸 잡고 뒤에 10라는 숫자 넣은 후, 앞의 빈 곳 0으로 채움. output_d는 양수. output_e는 음수. 부호가 있을 때는 맨 앞자리 부호로 채우고 나머지 빈 곳 0으로 채움

### 기호 붙여 출력하기

**소스 코드** | `format03.py` 

```python
# 양수
output_f = "{:+d}".format(10)
# 음수
output_g = "{:+d}".format(-10)
# 양수 : 기호 부분 공백
output_h = "{: d}".format(10)
# 음수 : 기호 부분 공백
output_i = "{: d}".format(-10)

print("# 기호와 함께 출력")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
```

{:+d}처럼 d앞에 + 기호 붙이면 양수와 음수 기호 표현.  
양수는 + 기호 표현. output_f 출력 결과 보면 쉽게 이해

{: d}처럼 앞에 공백 두고 기호 위치 비워 주면 함수 입력 기호 표현.  
10라는 숫자 기호 없이 넣었을 때 원래 “10”처럼 출력 output_h “10”로 출력

### 조합해 보기

**소스 코드** | `format04.py` 

```python
# 조합

# 기호를 뒤로 밀기 : 양수
output_h = "{:+5d}".format(10)
# 기호를 뒤로 밀기 : 음수
output_i = "{:+5d}".format(-10)
# 기호를 앞으로 밀기 : 양수
output_j = "{:=+5d}".format(10)
# 기호를 앞으로 밀기 : 음수
output_k = "{:=+5d}".format(-10)
# 0으로 채우기 : 양수
output_l = "{:=+05d}".format(10)
# 0으로 채우기 : 음수
output_m = "{:=+05d}".format(-10)

print("# 조합")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
```

기호와 공백 조합할 때는 = 기호 앞에 붙임.  
5칸의 공간 잡았을 떄 기호 빈칸 앞에 붙일 것인지, 숫자 앞에 붙일 것인지 지정하는 기호.

## 부동 소수점 출력의 다양한 형태

소수점 들어가는 float 자료형 숫자.  
float 자료형 출력을 강제로 지정할 때는 {:f} 사용 

### 다양한 형태의 부동 소수점 출력하기

**소스 코드** | `format05.py` 

```python
output_a = "{:f}".format(52.123)
output_b = "{:15f}".format(52.123)
output_c = "{:+15f}".format(52.123)
output_d = "{:+015f}".format(52.123)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
```

### 소수점 아래 자릿수 지정하기

**소스 코드** | `format06.py` 

실수형의 경우 소수점 아래 자릿수를 지정하는 기능.  
’.’을 입력 뒤에 몇 번째 자릿수까지 표시할지 지정

```python
output_a = "{:15.3f}".format(52.123)
output_d = "{:15.2f}".format(52.123)
output_c = "{:15.1f}".format(52.123)

print(output_a)
print(output_d)
print(output_c)
```

입력 15칸 잡고 소수점 각각 3자리, 2자리, 1자리 출력.  
이때 반 자동으로 반올림 하는 일 일어남

## 의미 없는 소수점 제거하기

Python 0과 0.0 출력했을 때 내부적으로 자료형 다르므로 서로 다른 값 출력. 그런데 의미 없는 0을 제거한 후 출려가혹 싶을 때format06가 있음.  
→ {:g} 사용

### 의미 없는 소수점 제거하기

**소스 코드** | `format07.py` 

```python
output_a = 10.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)
```

# 대소문자 바꾸기 : `upper()`와 `lower()`

**`upper()`** 함수는 문자열의 알파벳을 대문자로, **`lower()`** 함수는 문자열의 알파벳을 소문자로 만듬

`upper()` 함수

e.g. 변수 a에 저장된 문자열의 알파벳을 모두 대문자로 만듬

```python
>>> a = "Hello World"
>>> a.upper()
"HELLO WORLD"
```

`lower()` 함수

e.g. 변수 a에 저장된 문자열의 알파벳을 모두 소문자로 만듬

```python
>>>a.lower()
"hello world"
```

# 문자열 양옆 공백 제거하기 : `strip()`

strip() 함수 문자열 양옆 공백 제거.  
” 안녕하세요 ” → “안녕하세요” 

외쪽 공백을 제거하는 **`latrip()`** 함수 오른쪽 공백 제거하는 **`rstrip()`** 함수.

- **`strip()`**
    
    문자열 양옆 공백 제거
    
- **`lstrip()`**
    
    문자열 왼쪽 공백 제거
    
- **`rstrip()`**
    
    문자열 오른쪽 공백 제거
    

큰따옴표 또는 작은따옴표 세 번 반복한 기호 여러 줄 문자열 입력할 때 보기 쉽게 하려고 코드 작성하면 문자열 위아래에 의도하지 않은 줄바꿈

```python
>>> input_a = """
			안녕하세요
문자열의 함수 알아보기
"""
>>> print(input_a)
		
		안녕하세요
문자열 함수 알아보기
```

의도하지 않은 줄바꿈 및 문자열 양옆 공백은 `strip()` 함수로 쉽게 제거.

```python
>>> print(input_a.strip())
안녕하세요
문자열 함수 알아보기
```

코드 실행한 결과 보면 공백 제거 이전 줄바꿈 띄어쓰기가 들어감, 공백 제거 이후 모두 사라지는 것을 볼 수 있음. 공백 제거할 때 strip 활용.

참고 | `lstrip()` 함수의 `rstrip()` 함수 거의 사용하지 않음

# 문자열의 구성 파악하기 : `isOO()`

문자열 소문자로 구성,  알파벳으로만 구성되어 있는지, 숫자로만 구성되있는지 등 확인 is로 시작하는 이름 함수 사용.  

- **`isalnum()`**
    
    문자열 알파벳 또는 숫자로만 구성되어 있는지 확인.
    
- **`isalpha()`**
    
    문자열 알파벳으로만 구성 있는지 확인
    
- **`isidentifier()`**
    
    문자열 식별자로 사용할 수 있는 것인지 확인
    
- **`isdecimal()`**
    
    문자열 정수 형태 확인
    
- **`isdigit()`**
    
    문자열 숫자 인식될 수 있는 것인지 확인
    
- **`isspace()`**
    
    문자열 공백으로만 구성되어 있는지 확인
    
- **`islower()`**
    
    문자열 소문자로만 구성되어 있는지 확인
    
- **`isupper()`**
    
    문자열 대소문자로만 구성되어 있는지 확인
    

간단하게 몇 가지 사용.  
출력 True(맞다) or False(아니다)  
→ **불(boolean)**

```python
>>> print("TrainA10".isalnum())
True
>>> print("10".isdigit())
True
```

**`isalnum()`** 문자열 알파벳 또는 숫자로만 구성 확인하는 함수 “TrainA10”은 True, **`isdigit()`** 문자열 숫자로 인식될 수 있는 것인지 확인하는 함수 “10”도 True

# 문자열 찾기 : `find()`와 `rfind()`

문자열 내부 특정 문자 어디 위치하는지 확인할 때 **`find()`** 함수와 **`rfind()`** 함수 사용.

- **`firn()`**
    
    왼쪽부터 찾아서 처음 등장하는 위치 찾음
    
- **`rfirn()`**
    
    오른쪽부터 찾아서 처음 등장하는 위치 찾음
    

“안녕안녕하세요” 문자열 “안녕” 문자열 두개.  
왼쪽부터 찾았을 때와 오른쪽부터 찾았을 때의 위치 다릅

```python
>>> output_a = "안녕안녕하세요".find("안녕")
>>> print(output_a)
0
```

```python
>>> output_b = "안녕안녕하세요".rfind("안녕")
>>> print(output_b)
2
```

문자열 가장 앞글자 0번째라고 셈. 처음 “안녕”은 0번째 있는 것이고 두번째 “안녕”은 2번째부터 등장.  
→ 실행 결과 0과 2

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 안 | 녕 | 안 | 녕 | 하 | 세 | 요 |

# 문자열과 in 연산자

문자열 내부 어떤 문자열 있는 확인 in 연산자 사용.  
출력은 True(맞다) 또는 False(아니다)라 나옴

“안녕하세요” 문자열에 “안녕”포함? == True(맞다)

```python
>>> print("안녕" in "안녕하세요")
True
```

“안녕하세요”라는 문자열 “잘자”는 포함 X. == False(아니다) 출력

```python
>>> print("잘자" in "안녕하세요")
False
```

# 문자열 자르기 : `split()`

문자열 특정한 문자 자를 때는 `split()` 함수 사용.  
`split()` 함수 괄호 안 문자열 공백을 기준으로 자름

```python
>>> a = "10 20 30 40 50".split(" ")
>>> print(a)
['10', '20', '30', '40', '50']
```

실행 결과 **리스트(list)** 나옴.