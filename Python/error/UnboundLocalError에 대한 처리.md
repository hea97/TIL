### 재귀 함수로 구현한 피보나치 수열(3)

**소스 코드** | `fibonacci_recursion03.py` 

```python
conuter = 0

def fibonacci(n):
	counter += 1
	
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
	
	print(fibonacci(10))
```

위 코드 작성시 **UnboundLocalError** 예외 출력

```python
Traceback (most recent call last):
	File "fibonacci_recursion03.py", line 16, in <module>
		print(fibonacci(10))
	File "fibonacci_recursion03.py", line 6, in fibonacci
		counter += 1
UnboundLocalError: local variable 'counter' referenced before assignment
```

Python 함수 내부에서 함수 외부 있는 변수 참조하지 못해서 발생