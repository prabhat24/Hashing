
def largest_subarrys_contiguous_elements_m1(arr, N):
	# approach
	# 1. generate all the subarrays
	# 2. copy subarray into new memory location
	# 3. sort the new array
	# 5. itterate and find if array is contiguous
	# complexity - N^2 * (N+ NlogN + N)
	global_max = 1
	for i in range(0, N):
		for j in range(i, N):
			subarray = arr[i: j+1]
			subarray.sort()
			for k in range(0, len(subarray)-1):
				if subarray[k] + 1 != subarray[k+1]:
					break
				if k == len(subarray)-2:
					global_max = max(global_max, len(subarray))
	return global_max


def largest_subarrys_contiguous_elements_m2(arr, N):
	# approach
	# 1. generate all the subarrays
	# 3. sort the new array using insersion sort
	# 5. itterate and find if array is contiguous
	# complexity - N^2 * (N+ N)
	def insersion_sort(subarray, ele):
		subarray.append(ele)
		hole = len(subarray) - 1
		while hole > 0 and subarray[hole -1] > ele:
			subarray[hole] = subarray[hole -1]
			hole -= 1
		subarray[hole] = ele

	global_max = 1
	for i in range(0, N):
		subarray = []
		for j in range(i, N):
			insersion_sort(subarray, arr[j])
			for k in range(0, len(subarray)-1):
				if subarray[k] + 1 != subarray[k+1]:
					break
				if k == len(subarray)-2:
					global_max = max(global_max, len(subarray))
	return global_max	

def largest_subarrys_contiguous_elements_m3(arr, N):
	# approach
	# 1. generate all the subarrys
	# 2. find min, max in subarray by iterating
	# 3, ans = max - min + 1
	# complexity = N^2 * N	
	global_max = 1
	for i in range(0, N):
		for j in range(i, N):
			mina = 1<<31 - 1
			maxa = -1 * (1<<32 - 1)
			for k in range(i, j+1):
				maxa = max(maxa, arr[k])
				mina = min(mina, arr[k])
			if maxa - mina + 1 == j-i +1:
				global_max = max(global_max, maxa-mina+1)
	return global_max

def largest_subarrys_contiguous_elements_m4(arr, N):
	# approach
	# 1. generate all the subarrys
	# 2. find min, max in subarray by using carryforward technique
	# 3, ans = max - min + 1
	# complexity = N^2
	global_max = 1
	for i in range(0, N):
		mina = arr[i]
		maxa = arr[i]
		for j in range(i, N):
			maxa = max(maxa, arr[j])
			mina = min(mina, arr[j])
			if maxa - mina + 1 == j-i +1:
				global_max = max(global_max, maxa-mina+1)
	return global_max

if __name__ == "__main__":
	arr = [-1, 5, 3, 4, 6, -7, -4, -8, 16, 12, 18, 13, 15, 17, 14, 25, 10, 11]
	print(largest_subarrys_contiguous_elements_m1(arr, len(arr)))
	print(largest_subarrys_contiguous_elements_m2(arr, len(arr)))
	print(largest_subarrys_contiguous_elements_m3(arr, len(arr)))
	print(largest_subarrys_contiguous_elements_m4(arr, len(arr)))