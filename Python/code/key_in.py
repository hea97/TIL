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