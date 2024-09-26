pass 키워드 입력. 내일이면 잊어버림. raise 키워드와 미구현 상태 표현 NotImplementedError 조합 **raise NotlmplementedError** 사용 “아직 구현하지 않은 부분이에요!”라는 오류 강제로 발생

```python
number = input("정수 입력> ")
nubmer = int(number)

if nubmer > 0:
    # 미구현 상태
    raise NotImplementedError
else
		# 미구현 상태
		raise NotImplementedError
```

실행하면 코드 실행은 정상적으로 진행.  
순간 **NotlmplementedError**라는 오류 발생

‘이거 어제 구현 안했다라는 생각이 듬’

```python
정수 입력> 10
Traceback (most recent call last):
	File "passkeyword01.py", line 8, in <module>
		raise NotImplementedError
NotImplementedError
```