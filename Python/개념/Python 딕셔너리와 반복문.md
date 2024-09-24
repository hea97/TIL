# 딕셔너리 선언하기

딕션너리는 중괄호{} 선언, 키: 값 형태 쉼표(,) 연결해서 만듬.  
키는 문자열, 숫자, 불 등 선언.

딕셔너리 생성

---

변수 = {

키: 값,

키: 값,

. . .

키: 값

}

코드 적용

```python
>>> dict_a = {
	"name" : "캐치! 티니핑",
	"type" : "티니핑"
}
```

# 딕셔너리의 요소에 접근하기

```python
>>> dict_a
{'name' : '캐치! 티니핑', 'type', '티니핑'}
```

특정 키 값만 따로 출력.  
딕셔너리 요소 접근할 떄는 리스트처럼 딕셔너리 뒤 대괄호[] 입력, 내부 인덱스처럼 키 입력.   
이때 주의할 점 딕셔너리 선언할 때는 중괄호{} 사용, 딕셔너리 요소 접근할 때는 리스트처럼 딕셔너리 뒤에 대괄호[] 입력 내부 인덱스처럼 키 입력.

```python
>>> dict_a["name"]
'캐치! 티니핑'
>>> dict_a["type"]
'티니핑'
```

딕셔너리 내부 값 문자열, 숫자, 불 등 다양한 자료 넣을 수 있음. 리스트 딕셔너리 하나의 자료, 리스트 딕셔너리 값 넣을 수 있음

```python
>>> dict_b = {
				"director" : C
				"cast" : ["베베핑", "바로핑", "샤샤핑", "딱풀핑"]
}
```

```python
>>> dict_v
{'director' : ["하츄핑", "로미"], 'cast' : ["베베핑", "바로핑", "샤샤핑", "딱풀핑"]
}
>>> dict_b["director"]
["베베핑", "바로핑", "샤샤핑", "딱풀핑"]
```

| 구분 | 선언 형식 | 사용 예 | 틀린 예 |
| --- | --- | --- | --- |
| 리스트 | list_a[] | list_a[1] |  |
| 딕셔너리 | dict_a = {} | dict_a[”name”] | dict_a{”name”} |

### 딕셔너리의 요소에 접근하기

**소스 코드** | `dict01.py` 

```python
# 딕셔너리 선언
dictionary = {
    "name": "캐치! 티니핑",
    "type": "티니핑",
    "ingredient": ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
    "origin": "이모션 왕국"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "사랑의 하츄핑!"
print("name:", dictionary["name"])
```

ingredient는 dictionary의 키 또 여러 개의 자료 가지고 있는 리스트. 인덱스를 지정하여 리스트 안 특정 값 출력.

```python
>>> dictionary["ingredient"]
["베베핑", "바로핑", "샤샤핑", "딱풀핑"]
>>> dictionary["ingredient"][1]
"바로핑"
```

# 딕셔너리에 값 추가하기/제거하기

딕셔너리 값 추가할 때는 키 기반 값 입력

`딕셔너리[새로운 키] = 새로운 값` 

director에 새로운 자료 추가 다음 키를 정하고 값 입력.  
마지막 위치에 “price” 키 추가

```python
>>> director["price"] = 5000
>>> director
{'name': '사랑의 하츄핑!', 'type': "티니핑", 'ingredient': ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
"origin" : "이모션 왕국", 'price' : 5000} 
```

딕셔너리 이미 존재하고 있는 키 지정 값 넣으면 기존 값 새로운 값 대치하기도 함

```python
>>> director["name"] = '사랑의 하츄핑 로미!'
>>> director
{'name': '사랑의 하츄핑 로미!', 'type': "티니핑", 'ingredient': ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
"origin" : "이모션 왕국", 'price' : 5000} 
```

딕셔너리 요소 제거 또한 간단.  
리스트 때철머 **del 키워드** 사용 특정 키 지정 해당 요소 제거

```python
>>> del director["ingredient"]
>>> director
{'name': '사랑의 하츄핑 로미!', 'type': "티니핑", 
"origin" : "이모션 왕국", 'price' : 5000} 
```

### 딕셔너리에 요소 추가하기

**소스 코드** | `dict02.py` 

```python
dictionary = {}

print("요소 추가 이전 : ", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["name"] = "새로운 정신"
dictionary["name"] = "새로운 몸"

print("요소 추가 이후 : ", dictionary)
```

### 딕셔너리에 요소 제거하기

**소스 코드** | `dict03.py` 

```python
dictionary = {
	"name" = "캐치! 티니핑",
	"type" = "티니핑"
}
print("요소 제거 이전 : ", dictionary)

del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후 : ", dictionary)
```

# 딕셔너리 내부에 키가 있는지 확인하기

KeyError 발생. 존재하는 키인지, 존재하지 않는 키인지 확인할 수 있는 방법.

## in 키워드

리스트 내부 값 있는지 없는지 확인할 때 `in` 키워드 사용햇던 것처럼 딕셔너리 내부 키가 있는지 없는지 확인할 때도 **`in` 키워드** 사용

### 키가 존재하는지 확인하고 값에 접근하기

**소스 코드** | `key_in.py` 

```python
dictionary = {
    "name": "캐치! 티니핑",
    "type": "티니핑",
    "ingredient": ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
    "origin": "이모션 왕국"
}

key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키")
```

## `get()` 함수

키에 접근하는 상황 대한 두 번째 대체 방법는 딕셔너리 **`get()`** 함수 사용하는 방법.  
이전 문자열 내부적으로 많은 함수 갖고 있는 것을 확인. 딕셔너리 뒤 . 찍고 자동 완성 기능 확인하면 다양한 기능 있다는 것을 알 수 있음.

`get()` 함수 딕셔너리 키로 값 추출하는 기능 딕셔너리[키] 입력할 때와 같은 기능 수행, 존재하지 않는 키 접근할 경우 KeyError 발생시키지 않고 **None** 출력

### 키가 존재하지 않을 때 None 출력하는지 확인

**소스 코드** |  `get01.py` 

```python
dictionary = {
    "name": "캐치! 티니핑",
    "type": "티니핑",
    "ingredient": ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
    "origin": "이모션 왕국"
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value is None:
    print("존재하지 않는 키에 접근.")
```

# `for` 반복문 : 딕셔너리와 함께 사용하기

`for` 반복문과 딕셔너리 조합.  
`for` 반복문과 딕셔너리 조합 사용  
주의 점 딕셔너리 내부 있는 키 변수 들어간다는 것.

---

for 키 변수 in 딕셔너리:

코드

---

### for 반복문과 딕셔너리

**소스 코드** |  `for_dict.py` 

```python
dictionary = {
    "name": "캐치! 티니핑",
    "type": "티니핑",
    "ingredient": ["베베핑", "바로핑", "샤샤핑", "딱풀핑"],
    "origin": "이모션 왕국"
}

for key in dictionary:
    print(key, ":", dictionary[key])
```