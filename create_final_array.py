# given array of length N and Q queries including i & j & x.
# each of the Q queries gives constant step function x from arr[i] to arr[j].
# find the output signal thus formed.
# - 10^9 <= x <= 10 * 9
# where 0 <= i,j < N.

def create_array(arr, Q):
	for q in Q:
		i, j, x = q
		# create +ve impulse function at i
		arr[i] += x
		# create -ve impulse function at j + 1
		if j < len(arr)-1:
			arr[j+1] -= x

	suma = 0
	for i in range(0, len(arr)):
		suma += arr[i]
		arr[i] = suma
	return arr

if __name__ == '__main__':
	arr = [0] * 10
	Q = [
		(1,4,2,),
		(3,5,6,),
		(0,7,-3,),
		(6,9,5),
	]
	print(create_array(arr, Q))