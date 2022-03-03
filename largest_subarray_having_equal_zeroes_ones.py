def sol_m1(arr, N):
	# 2 pointers and carry forward
	maxa = 0
	for i in range(0, N):
		suma = 0
		for j in range(i+1, N, 2):
			suma += arr[j-1] + arr[j]
			if suma == (j - i + 1)//2:
				maxa = max(maxa, j-i+1)
	return maxa


def sol_m2(arr, N):
	# hash maps
	# replace 0 with -1
	# create presum array (insert 0 at head).
	# create a hash map for first occurance, last occurance of the value in presum array index.
	# itterate the hash map for all the occurances and find out the largest length of presum array.
	presum = [0] * (N + 1)
	suma = 0
	hash_map = {}
	hash_map[0] = [0, 0]
	for i in range(1, N+1):
		if arr[i - 1] == 0:
			suma -= 1
		else:
			suma += 1
		presum[i] = suma
		occurance = hash_map.get(presum[i], None)
		if occurance:
			fo, lo = occurance[0], occurance[1]
			if i < fo:
				fo = i
			if i > lo:
				lo = i
			occurance = [fo, lo]
		else:
			occurance = [i, i]
		hash_map[presum[i]] = occurance
	maxa = 0
	for key in hash_map.keys():
		fo, lo= hash_map[key]
		maxa = max(maxa, lo - fo)
	return maxa

if __name__ == '__main__':
	arr = [0, 1, 0, 1, 0, 1, 1, 0]
	print(sol_m1(arr, len(arr)))
	print(sol_m2(arr, len(arr)))


		

