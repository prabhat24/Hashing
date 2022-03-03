# find minimum of |arr[i] + arr[j] -k|  

def find_minimum_sum_pair_m1(arr, N, k):
	# check for all the pairs and find minimum
	# complexity - O(Nˆ2), 1
	mina = 1<<31 - 1
	for i in range(0, N-1):
		for j in range(i+1, N):
			mina = min(abs(arr[i] + arr[j] - k), mina)
	return mina


def find_minimum_sum_pair_m2(arr, N, k):
	# sort the array
	# take 2 pointers start and end
	# if arr[i] + arr[j] < k => increment st++
	# elif arr[i] + arr[j] > k => decrement end --
	# elif arr[i] + arr[j] == k => return 0
	# complexity - NlogN + N, 1

	arr.sort()
	mina = 1<<31 - 1

	st = 0
	end = N-1

	while(st<end):
		mina = min(abs(arr[st] + arr[end] - k), mina)
		# print(mina, st, end)
		if arr[st] + arr[end] < k:
			st += 1
		elif arr[st] + arr[end] > k:
			end -= 1
		elif arr[st] + arr[end] == k:
			return 0
	return mina

def find_minimum_sum_pair_m3(arr, N, k):
	# sort the array
	# start iterating from i=0 to i=(N-1)
	# for each iteration fix arr[i]
	# to find arr[j] use binary search such that arr[i] + arr[j] is closest to k
	# ie. if arr[i] + arr[mid] < k increment st
	# and if arr[i] + arr[mid] > k decrement end
	# maintain minimum

	# complexity - NlogN + NlogN, 1 
	arr.sort()
	mina = 1<<31 -1
	for i in range(0, N-1):
		st = i+1
		end = N-1
		while st<=end:
			mid = (st + end)//2
			if arr[i] + arr[mid] < k:
				st += 1
			elif arr[i] + arr[mid] > k:
				end -= 1
			elif arr[i] + arr[mid] == k:
				return 0
		mina = min(mina, abs(arr[i] + arr[mid] - k))
	return mina


if __name__ == '__main__':
	arr = [5, 1, 12, -3, 8, 15, -9, 2, 21]
	print(find_minimum_sum_pair_m1(arr, len(arr), 30))
	print(find_minimum_sum_pair_m2(arr, len(arr), 30))
	print(find_minimum_sum_pair_m3(arr, len(arr), 30))
