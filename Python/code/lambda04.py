books = [{
	"제목" : "혼자 공부하는 Python",
	"가격" : 18000
}, {
	"제목" : "혼자 공부하는 머신러닝 + 딥러닝",
	"가격" : 26000
}, {
	"제목" : "혼자 공부하는 Java",
	"가격" : 24000
}]

def 가격추출함수(book):
	return book["가격"]
	
print("# 가장 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
	print(book)