def sol_m2(A, B, C):
	A.sort()
	B.sort()
	C.sort()

	i = 0
	j = 0
	k = 0


	mina = 1<<31 - 1
	while i<len(A) and j<len(B) and k<len(C):
		mina = min(mina, max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]) )
		if A[i] <= min(B[j], C[k]):
			i += 1
			continue
		if B[j] <=  min(A[i], C[k]):
			j += 1
			continue
		if C[k] <=  min(A[i], B[j]):
			k += 1
			continue
	return mina


if __name__ == '__main__':
	A = [5, 1, 8, 2, 17, 12, 5]
	B = [1, 7, 3, 18, 5, 17, 6]
	C = [12, 9, 4, 21, 18, 10, 13]
	print(sol_m2(A, B, C))