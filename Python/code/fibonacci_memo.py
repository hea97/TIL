dictionary = {
	1 : 1,
	2 : 1
}

def fibonacci(n):
	if n in dictionary:
		return dictionary[n]
	else:
		output = fibonacci(n - 1) + fibonacci(n - 2)
		dictionary[n] = output
		return output

print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(20) : ", fibonacci(20))
print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))
print("fibonacci(50) : ", fibonacci(50))