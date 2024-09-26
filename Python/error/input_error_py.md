```python
# 입력 받기
string = input("입력> ")

# 출력
print("입력 + 100 : ", string + 100)
```

```python
입력> 300 |Enter|
traceback (most recent call last):
	File "inputerror.py" line 5, in <module>
		print("입력 + 100 : ", string + 100)
TypeError: can only concatenate str (not "int") to str
```

입력 받은 값 300과 100을 더하고자 한 것이었으나 `input()` 함수로 입력받은 자료는 모두 문자열로 저장되므로 “300” + 100 되어 문자열 숫자는 더할 수 없어 발생한 오류.  
입력받은 문자열 숫자 변환 숫자 연산 활용