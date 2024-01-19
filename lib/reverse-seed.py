
for a in range(10, 99):
	for b in range(10, 99):
		ab = str(a * b)
		straight_a = str(a)
		straight_b = str(b)
		reverse_a = str(a)[::-1]
		reverse_b = str(b)[::-1]
		reverse_seed = reverse_a + straight_b
		if ab == reverse_seed:
			print(a, b, ab, reverse_seed)
