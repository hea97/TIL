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