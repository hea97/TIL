```python
>>> print("Hello" + 10)
```

문자열 + 숫자 → **`TypeError: can only concatenate str (not “int”) to str`**  ****오류(error) 남

---

문자열은 무조건 문자열끼리 + 연산자를 사용 연결, 숫자여도 문자열과 함께 + 연산하려면 큰따옴표 붙여 문자열 인식시켜야만 오류 없이 결과 얻음. 숫자를 더할 때는 반드시 숫자와 숫자 사이에 + 연산자를 사용해 연산

```python
>>> print("Hello" + "10")
Hello10
```

문자열 연결 연산자 → **많이 사용하는 연산자 기억하기**