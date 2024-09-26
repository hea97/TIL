자료형 반환할 때 ‘변환할 수 없는 것’을 변환하려고 하면 **ValueError** 예외 발생. 예외 발생 이유 두 가지

## 1. 숫자가 아닌 것을 숫자로 변환하려고 할 때

---

`int(”Hello”)`

`flaot(”Hello”)`

---

코드 실행하면 곧바로 예외 발생.  
”Hello”라는 문자열 `int()` 함수 변환할 수 없는 값이기 때문. 함수의 괄호 안 넣는 것을 매개변수라 부름, `int()` 함수와 `float()` 함수는 매개변수로 변환할 수 없는 형태 들어가면 항상 오류 발생

int_convert.py를 실행한 후 ‘입력A> ’의 데이터 입력할 때 “Hello”라고 입력하면 이 자료는 아예 숫자로 변환할 수 없으므로 다음과 같은 오류 발생

```python
Traceback (most recent call last):
	FIle "int_convert.py", line 2, in <module>
		int_a = int(string_a)
ValueError: invalid literal for int() with base 10: Hello
```

## 2. 소수점이 있는 숫자 형식의 문자열을 `int()` 함수로 변환하려고 할때

`int(”5.55”)` 

int 정수형 실수형 자료를 정수형으로 바꾸라 하면, 오류가 발생.

int_convert.py 실행한 후 ‘입력A> ’의 데이터 입력할 때 5.55이라는 실수형 자료를 입력하면 이 자료 정수형 변환할 수 없으므로 당므과 같은 오류 메시지 나옴

```python
Traceback (most recent call last):
	File "int_convert.py", line 2, in <module>
		int_a = int(string_a)
ValueError: invalid literal for int() with base 10: 5.55
```