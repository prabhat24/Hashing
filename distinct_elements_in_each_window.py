# given array of size N and window k,
# count and print no if distinct elements in each window


def distinct_ele_m1(arr, N, k):
	# algorithm
	# 1. iterate the array from i=0 , i=N-K
	# 2. for each iteration put element from i to i+k-1 to the set
	# 3. Print the size of the set
	# complexity = (N-k+1)*k
	s = set()
	for i in range(0, N-k+1):
		for j in range(i, i+k):
			s.add(arr[j])
		print(len(s))
		s.clear()

def distinct_ele_m2(arr, N, k):
	# algorithm
	# 1. iterate the array from i=0 , i=N-K
	# 2. for each iteration put element from i to N to the set
	# 3. Print the size of the set
	# complexity = (N-k+1)
	hash = {}
	i = 0
	while i < k:
		if hash.get(arr[i], None):
			hash[arr[i]] += 1
		else:
			hash[arr[i]] = 1
		i+=1
	print(len(hash))
	for i in range(k, N):
		hash[arr[i-k]] -= 1
		if hash[arr[i-k]] == 0:
			hash.pop(arr[i-k])
		if hash.get(arr[i], None):
			hash[arr[i]] += 1
		else:
			hash[arr[i]] = 1
		print(len(hash))

if __name__ == '__main__':
	arr = [-1, 5, 2, 6, 2, 2, 6, 7, -6, 7, 2]
	distinct_ele_m1(arr, len(arr), 4)
	print("_______")
	distinct_ele_m2(arr, len(arr), 4)