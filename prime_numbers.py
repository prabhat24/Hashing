# Prime Numbers
# find all prime numbers between x to y
 

# create sieve of primes

def prime_number_m3(N):
	# create a hash for storing wheter a number is prime or not.
	# assuming all the numbers are prime initially
	hash = [True,] * (N+1)
	
	# iterate from x to y taking each number as divisor.
	# and mark all the multiples of x as not prime
	i = 2
	while i * i <= N:
		if hash[i]:
			for j in range(i*i, N+1, i):
				hash[j] = False
		i = i + 1
	return hash

if __name__ == '__main__':
	print(prime_number_m3(20)[:20])
