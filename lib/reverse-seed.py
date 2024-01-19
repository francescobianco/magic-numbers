
for a in range(10, 99):
	for b in range(10, 99):
		ab = str(a * b)
		reverse_seed = str(b)[::-1] + str(a)[::-1]
		if ab == reverse_seed:
			print(a, b, ab, reverse_seed)
