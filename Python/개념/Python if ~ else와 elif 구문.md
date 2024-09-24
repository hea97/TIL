# `else` 조건문의 활용

프로그래밍 언어는 **else 구문** 이라는 기능 제공.  
else 구문은 if 조건문 뒤 사용하며, if 조건문의 조건이 거짓일 때 실행되는 부분.

---

if 조건:    

    조건이 참일 때 실행할 문장

else:

    조건이 거짓일 때 실행할 문장

---

`condition03.py` 예제에 else 구문 넣어 홀 짝 비교

### `if` 조건문에 `else` 구문을 추가해서 짝수와 홀수 구분하기

**소스 코드** | `condition04.py` 

```python
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
	    print("짝")
else:
	    print("홀")
```

`if else`구문을 사용하면 조건 비교를 한 번만 하므로 이전의 코드보다 두 배 효율적이라 할 수 있음. → 조건 비교가 많아질 수록 시간 차가 크게 발생하므로 효율적으로 만드는게 중요

# `elif` 구문

세 개 이상의 조건을 연결해서 사용하는 방법 필요.   
**`elif` 구문**

elif구문은 if 조건문과 else 구문 사이 입력.

---

if 조건A:

    조건A가 참일 때 실행할 문장

elif 조건B:

    조건B가 참일 때 실행할 문장

elif 조건C:

    조건C가 참일 때 실행할 문장

else:

    모든 조건이 거짓일 때 문장

---

### 계절 구하기

**소스 코드** | `condition05.py` 

```python
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")
```

# `if` 조건문을 효율적으로 사용하기 (누적 예제)

e.g. 학점과 학점에 대한 학생 평가

| 조건 | 설명 | 조건 | 설명 |
| --- | --- | --- | --- |
| 4.5 | 신 | 1.75 ~ 2.3 | 오락문화의 선구자 |
| 4.2 ~ 4.5 | 교수님의 사랑 | 1.0 ~ 1.75 | 불가촉천민 |
| 3.5 ~ 4.2 | 현 체제의 수호자 | 0.5 ~ 1.0 | 자벌레 |
| 2.8 ~ 3.5 | 일반인 | 0 ~ 0.5 | 플랑크톤 |
| 2.3 ~ 2.8 | 일탈을 꿈꾸는 소시민 | 0 | 시대를 앞서가는 혁명의 씨앗 |

### 유머를 조건으로 구현하기(1)

**소스 코드** | `condition06.py` 

```python
score = float(input("학점 입력> "))

if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif 0 <= score < 0.5:
    print("플랑크톤")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗")
```

if 조건문은 위에서 아래로 흐르며, else 구문과 elif 구문은 이전의 조건이 맞지 않을 떄 넘어오는 부분.  
이미 제외된 조건을 한 번 더 검사할 필요 없음

### 유머를 조건으로 구현하기(2)

**소스 코드** | `condition07.py` 

```python
score = float(input("학점 입력> "))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 <= score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")
```

비교해서 거짓임을 확인하고 실행하고 있으므로 하위 값만 검사하고 상위 값만 검사를 생략.

`elif 4.2 ≤ socre < 4.5:` → `elif 4.2 ≤ score:`

코드 가독성도 좀 더 향상되기 때문에 프로그램 효율이 훨씬 높아짐.  

# False로 변환하는 값

`if` 조건문 매개변수 불 아닌 값이 올 때는 자동으로 이를 불로 변환해서 처리.  
어떤 값이 True 변환, 어떤 값이 False 변환되는지 알고 있어야 코드를 이해할 수 있음.  
False 변환되는 값은 None, 숫자 0과 0.0 **빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)**. 모두 Ture 변환되므로 위 세 가지만 기억.

### Fasle로 변환되는 값

**소스 코드** | `false_value.py` 

```python
print("# 조건문 0 넣기")
if 0:
    print("0은 True 변환")
else:
    print("0은 False 변환")
    print()

print("# if 조건문 빈 문자열 넣기")
if "":
    print("빈 문자열은 True")
else:
    print("빈 문자열은 False")
```

# `pass` 키워드

프로그래밍 하다 보면 일단 프로그래밍 전체 골격 잡아 놓고 내부 처리 할 내용을 차근차근 생각.  
골격은 일반적으로 조건문, 반복문, 함수, 클래스 등의 기본 구문

---

if zero == 0    

else:   

---

### 나중에 구현하려고 비워 둔 구문

**소스 코드** | `pass_keyword.py` 

```python
number = input("정수 입력> ")
nubmer = int(number)

if nubmer > 0:
    
else

```

Python if 조건문 사이에는 무조건 들여쓰기 4칸 넣고 코드 작성해야만 구문 성립. 이렇게 작성하면 **IndentationError** 발생

### pass 키워드를 사용한 미구현 부분 입력

**소스 코드** | `pass_keyword01.py` 

```python
number = input("정수 입력> ")
nubmer = int(number)

if nubmer > 0:
    
    pass
else:
		pass
```

### `raise NotImplementedError`
pass 관련 error