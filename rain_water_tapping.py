


def rain_water_tapping(arr, N):
	ml = [0] * N
	mr = [0] * N
	for i in range(1, N):
		ml[i] = max(ml[i-1], arr[i-1])

	for i in range(N-2, 0, -1):
		mr[i] = max(mr[i+1], arr[i+1])

	water_trapped = 0
	for i in range(0, N):
		if min(mr[i], ml[i]) - arr[i] > 0:
			water_trapped += min(mr[i], ml[i]) - arr[i]
	return water_trapped



if __name__ == '__main__':
	arr = [0, 2, 1, 3, 0, 1, 2, 1, 2, 1]
	print(rain_water_tapping(arr, len(arr)))
