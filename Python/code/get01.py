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