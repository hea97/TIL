import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")
