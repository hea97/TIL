함수 생성할 때 매개변수 만듬, 함수 호출할 때 매개변수를 넣지 않거나 더 많이 넣으면 어떻게 될까?

### 매개변수 넣지 않은 경우

```python
def print_n_times(value, n)
	for i in range(n):
		print(value)
print_n_times("Hello")
```

오류 출력. print_n_times()  라는 함수 매개변수 n이 없다.라는 오류.

자주 발생하는 오류 중 하나

```python
Traceback (most recent call last):
	File "test5_01.py", line 6, in <module>
		print_n_times("Hello")
TypeError: print_n_times() missing 1 required positional argument: 'n'
```

### 지정 개수보다 매개변수 더 많이 넣은 경우

```python
def print_n_times(value, n):
	for i in range(n):
		print(value)
print_n_times("Hello", 10, 20)
```

오류 출력. print_n_times() 함수는 2개의 매개변수가 필요, 3개가 들어왔다는 오류. → 함수 호출할 때 함수 선언할 때와 같은 개수 매개변수 입력

```python
Traceback (most recent call last):
	File "test5_02.py", line 6, in <module>
		print_n_times("Hello", 10, 20)
TypeError: print_n_times() takes 2 positional arguments but 3 were given
```