def sumFib(asum):
	x = y = 1
	sum = 0
	while (sum < asum):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum

print(sumFib(4000000))