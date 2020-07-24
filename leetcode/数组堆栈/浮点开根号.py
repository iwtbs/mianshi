def sqrt1(n):
	min = 0
	max = n
	mid = n / 2
    PRECISION = 0.0002
    while (mid*mid>n + PRECISION or mid*mid<n - PRECISION):
		mid = (max + min) / 2
		if (mid*mid < n + PRECISION):
			min = mid #根值偏小，升高下边界
		elif (mid*mid > n - PRECISION):
			max = mid#根值偏大，降低上边界
	return mid