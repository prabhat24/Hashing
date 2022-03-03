# given 2 sorted arrays find the median

def sol_m1(arr1, arr2 , N,  M):
	i, j, k = 0, 0, 0
	res = [0] * (N+M)

	while i<N and j<M:
		if arr1[i] <= arr2[j]:
			res[k] = arr1[i]
			i+=1
		else:
			res[k] = arr2[j]
			j+=1
		k += 1
	while i<N:
		res[k] = arr1[i]
		i+=1
		k+=1

	while j<M:
		res[k] = arr2[j]
		j+=1
		k+=1
	if (N+M) % 2 == 0:
		return res[(N+M)//2-1]
	else:
		return res[(N+M)//2]
	


def sol_m2(arr1, arr2, N, M):
	i, j, k = 0, 0, 0
	threshold = 0
	if (N+M) % 2 == 0:
		threshold=(N+M)//2
	else:
		threshold=(N+M)//2 + 1
	while i<N and j<M and k < threshold-1:
		if arr1[i] <= arr2[j]:
			i+=1
		else:
			j+=1
		k += 1
	while i<N and k<threshold-1:
		i+=1
		k+=1

	while j<M and k<threshold-1:
		j+=1
		k+=1
	return min(arr1[i], arr2[j])

def get_elements_less_than_mid(arr, key):
	if key > arr[-1]:
		return len(arr)
	if key < arr[0]:
		return 0
	st = 0
	end = len(arr) - 1
	ans = 0
	while st<=end:
		mid = (st + end)//2
		if arr[mid] < key:
			st = mid + 1
		elif arr[mid] >= key:
			ans = mid
			end = mid - 1
	return ans

def get_elements_greater_than_mid(arr, key):
	if key > arr[-1]:
		return 0
	if key < arr[0]:
		return len(arr)
	st = 0
	end = len(arr) - 1
	while st<=end:
		mid = (st + end)//2
		if arr[mid] <= key:
			ans = mid
			st = mid + 1
		elif arr[mid] > key:
			end = mid - 1
	return len(arr) - (ans + 1)

def sol_m3(arr1, arr2, N, M):
	st = min(arr1[0], arr2[0])
	end = max(arr1[-1], arr2[-1])
	lt_elements, gt_elements = 0, 0 
	if (N + M)%2:
		lt_elements = (N + M)//2
		gt_elements = (N + M)//2
	else:
		lt_elements = (N + M)//2 - 1
		gt_elements = (N + M)//2

	while st<=end:
		mid = st + (end - st)//2
		print("st, end, mid", st, end, mid)
		l1 = get_elements_less_than_mid(arr1, mid)
		l2 = get_elements_less_than_mid(arr2, mid)
		g1 = get_elements_greater_than_mid(arr1, mid)
		g2 = get_elements_greater_than_mid(arr2, mid)
		print("l1, l1", l1, l2)
		print("g1, g2", g1, g2)
		if l1 + l2 < lt_elements:
			st = mid + 1
		elif l1 + l2 > lt_elements:
			end = mid - 1
		elif g1 + g2 < gt_elements:
			end = mid - 1
		elif g1 + g2 > gt_elements:
			st = mid + 1
		elif l1 + l2 == lt_elements and g1 + g2 == gt_elements:
			ans = mid
			break
	return ans



if __name__ == '__main__':
	arr1 = [-1, 5, 7, 12, 18, 30, 53, 71]
	arr2 = [-6, -3, 0, 8, 23]
	print(sol_m1(arr1, arr2, len(arr1), len(arr2)))
	print(sol_m2(arr1, arr2, len(arr1), len(arr2)))
	print(sol_m3(arr1, arr2, len(arr1), len(arr2)))