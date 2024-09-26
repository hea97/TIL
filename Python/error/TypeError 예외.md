서로 다른 자료 연산 **TypeError** 예외 발생.  
문자열과 숫자를 그대로 입력했을 때 자료형 눈으로 바로 확인할 수 있으므로 서로 다른 자료 연산하는 실수 거의 없음.  
변수를 사용 내부에 무슨 자료가 들어 있는지 바로 확인할 수 없으므로 TypeError 발생.

```python
>>> string = "문자열"
>>> number = 10
>>> string + number
```

문자열과 숫자를 + 연산자 연결.  
문자열은 + 연산자 **문자열 연결 연산자** 사용, 숫자 + 연산자 **덧셈 연산자** 사용하려다 충돌 발생

자주 발생하는 오류

```python
Traceback (most recent call last):
	File "<pyshell#3>", line 1, in <module>
		string+number
TypeError: can only concatenate str (not "int") to str
```