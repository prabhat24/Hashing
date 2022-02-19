def max_sum_subarray_m1(arr, N):
	# approach -
	# 1. generate all the subarrays of the array
	# 2. check if the new array gives the max sum by iterating again
	# complexity - N^2 * N, 1
	global_max = arr[0]
	st_ind = 0
	end_ind = 0
	for i in range(0, N):
		for j in range(i, N):
			suma = 0
			for k in range(i, j+1):
				suma += arr[k]
			if suma > global_max:
				global_max = suma
				st_ind = i
				end_ind = j
	return global_max, (st_ind, end_ind,)


def max_sum_subarray_m2(arr, N):
	# approach -
	# 1. generate all the subarrays of the array
	# 2. check if the new array gives the max sum by using carryforwad technique.
	# complexity - N^2 * N, 1
	global_max = arr[0]
	st_ind = 0
	end_ind = 0
	for i in range(0, N):
		suma = 0
		for j in range(i, N):
			suma = suma + arr[j]
			if suma > global_max:
				global_max = suma
				st_ind = i
				end_ind = j
	return global_max, (st_ind, end_ind,)



def max_sum_subarray_m3(arr, N):
	# approach
	# 1. create the presum array (now problem becomes similar to buy sell stock to gain max profit)
	# 2. find the lowest point to sell and then highest point to buy
	# complexity -  N + N*N  , N + 1
	pre_sum = [0] * len(arr)
	suma = 0 
	for i in range(0, N):
		suma = suma + arr[i]
		pre_sum[i] = suma

	global_max = max(arr)
	for i in range(0, len(pre_sum) -1):
		for j in range(i+1, len(pre_sum)):
			global_max = max(global_max, pre_sum[j] - pre_sum[i])
	return global_max


def max_sum_subarray_m4(arr, N):
	# approach
	# 1. create the presum array (now problem becomes similar to buy sell stock to gain max profit)
	# 2. find the lowest point to sell and then highest point to buy
	# complexity -  N + N  , N + 1
	pre_sum = [0] * len(arr)
	suma = 0 
	for i in range(0, N):
		suma = suma + arr[i]
		pre_sum[i] = suma

	global_max = max(arr)
	max_rate_so_far = -1 * (2 << 32 -1)
	for i in range(len(pre_sum) -1, -1, -1):
		max_rate_so_far = max(pre_sum[i], max_rate_so_far)
		global_max = max(global_max, max_rate_so_far-pre_sum[i])
	return global_max



if __name__ == '__main__':
	arr = [-2, -3, 4, -1, 2, 10, -5, -3]
	print(max_sum_subarray_m1(arr, len(arr)))
	print(max_sum_subarray_m2(arr, len(arr)))
	print(max_sum_subarray_m3(arr, len(arr)))
	print(max_sum_subarray_m4(arr, len(arr)))

