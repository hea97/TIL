프로그래밍 할 때 가장 많이 만나는 예외 중 하나 **IndexError(index out of range)** 예외.    
모든 프로그래밍 언어 주요 예외 중 하나이다.

IndexError 예외는 리스트/문자열 수를 넘는 요소/글자 선택할 때 발생.  
문자열로 e.g.

e.g. “Hello”라는 다섯 글자에서 10번째 문자 접근.  
즉, 문자열 없는 문자를 선택하고 있으므로 인덱스가 범위를 넘었다 해서 index out of range라는 오류 발생

```python
>>> print("Hello"[10])
```

```python
Traceback (most recent call last):
	File "<pyshell#2>", line 1, in <module>
		print("Hello"[10])
IndexError: index out of range
```

`<pyshell#2>`  python IDLE 에디터 실행했을 때 나타나는 내용 에디터마다 다르게 나타남

코드 작성하다 예외 발생하면 ‘리스트/문자열 수 넘는 부분 선택’했다라고 인지하기