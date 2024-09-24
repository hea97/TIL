def print_n_times(n, *values):
	for i in range(n):
		for value in values:
			print(value)
		print()
print_n_times(3, "Hello", "World", "Python")