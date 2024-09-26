리스트 길이 넘는 인덱스 접근 INdexError 발생.  
딕셔너리 존재하지 않는 키 접근하면 마찬가지로 **KeyError** 발생.

```python
>>> dictionary = {}
>>> dictionary["Key"]
```

```python
Traceback (most recent call last):
	File "<pyshell#7>", line 1, in <module>
		dictionary["Key"]
KeyError: 'Key'
```

리스트 ‘인덱스’ 기반 값 저장 IndexError, 딕셔너리 ‘키’ 기반 값 저장 KeyError 발생.

```python
>>> del dictionary["Key"]
Traceback (most recent call last):
	File "<pyshell#8>", line 1, in <module>
		del dictionary["Key"]
KeyError: 'Key'
```