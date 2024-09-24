# 날짜/시간 관련된 기능 가져옴
import datetime

# 현재 날짜/시간 구함
now = datetime.datetime.now()

if now.hour < 12:
	    print("현재 시각은 {}시로 오전.".format(now.hour))
if now.hour >= 12:
	    print("현재 시각은 {}시로 오후.".format(now.hour))