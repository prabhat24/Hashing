def smallest_substring(A, B):
	st = 0
	end = 0
	global_min = 1<<31 -1
	g_st = 0
	g_end = 0
	# find hash of B
	hash_b = {} 
	for i in range(0, len(B)):
		hash_b[B[i]] = hash_b.get(B[i], 0) + 1

	hash_a = {}
	match_count = 0
	print(hash_b)
	while True: 
		f = False
		# acquire
		while end<len(A) and match_count<len(B):
			# print("1-------")
			# print("st", st, "end", end)
			if hash_a.get(A[end], 0) < hash_b.get(A[end], 0):
				match_count += 1
			hash_a[A[end]] = hash_a.get(A[end], 0) + 1
			end += 1
			# print(hash_a, match_count)
			f = True
		# release
		while st<=end and match_count==len(B):
			print(global_min)
			if end - st <= global_min:
				g_st = st
				g_end = end - 1
				global_min = g_end - g_st + 1
			hash_a[A[st]] = hash_a.get(A[st], 0) - 1
			if hash_a.get(A[st], 0) < hash_b.get(A[st], 0):
				match_count -= 1
			# print(hash_a, match_count)
			st += 1
			f = True
		if f == False:
			break
	return global_min, g_st, g_end	

if __name__ == '__main__':
	A = "xysmsstamyzamstsamast"
	B = "samsta"
	print(smallest_substring(A,B))
	