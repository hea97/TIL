문자열 IndexError 예외.  
이 예외는 리스트 길이를 넘는 인덱스 요소 접근할 때 발생하는 예외. 요소 존재하지 않는 위치 요소 꺼내려고 하니 예외 발생

```python
>>> list_a = [1,2,3]
>>> list_a[3]
```

list_a[3] 요소 없으므로 IndexError 예외 발생

```python
Traceback (most recent call last):
	File "<pyshell#3>", line 1, in <module>
IndexError: list index out of range
```