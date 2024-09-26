{} 기호 개수 `format()` 함수의 매개변수 개수보다 많으면 **IndexError** 예외 발생.

매개변수가 {}보다 많은 경우 {} 개수만큼 적용되고 나머지 매개변수는 버려짐.  
그래서 아무 문제 없이 실행. 두 번째 {} 매개변수 많은 경우 IndexError 예외 발생

```python
>>> "{} {}".format(1, 2, 3, 4, 5)
'1, 2'
>>> "{} {} {}".format(1, 2)

Trackback (most recent call last):
	File "<pyshell#1>", line 1, in <module>
		"{} {} {}.format(1, 2)"
IndexError: tuple index out of range
```