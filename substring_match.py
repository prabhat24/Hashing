# given 2 strings and Q queries, each query contains 4 parmeters i, j, k, l
# find string1.substring(i, j) == string2.substing(k,l)
# eg
# string 1 - "abfreqaghanaapsssbt"
# string 2 - "aaghanaasfcxch"
# Q queries follows
# i j k l
# 1 8 5 12
# 2 6 4 8
# 3 9 0 6


class Solution():
	
	# P1 = 37
	# P2 = 97
	k = 1<<31 - 1
	def __init__(self, string1, string2):
		N = len(string1)
		M = len(string2)
		self.power1 = self.precompute_power(max(N,M), 37)
		self.ha1 = self.find_hash_sum(string1, self.power1)
		self.ha2 = self.find_hash_sum(string2, self.power1)

	
	def precompute_power(self, l, P):
		power = [1] * (l + 1)
		for i in range(1, l+1):
			power[i] = (power[i-1] * P) % self.k
		return power

	@staticmethod
	def ascii(ch):
		return ord(ch) - ord('a')

	def find_hash_sum(self, string, p):
		h = [0] * len(string)
		h[0] = self.ascii(string[0]) * p[1]
		for i in range(1, len(string)):
			h[i] = ( h[i-1] + ( self.ascii(string[i]) * p[i+1] ) % self.k ) % self.k
		return h

	def match(self, i, j, k, l):
		hash_val1 = (self.ha1[j] - self.ha1[i-1] + self.k) % self.k if i > 0 else self.ha1[j]
		hash_val2 = (self.ha2[l] - self.ha2[k-1] + self.k) % self.k if k > 0 else self.ha2[l]
		if i > k:
			hash_val2 = (hash_val2 * self.power1[i-k]) % self.k
		else:
			hash_val1 = (hash_val1 * self.power1[k-i]) % self.k
		if hash_val1 == hash_val2:
			return True
		return False

if __name__ == '__main__':
	string1 = "axymsayzrtxxzmnoprbdac"
	string2 = "azyzrtxzoprbmnxoy"
	sol = Solution(string1, string2)
	print(sol.match(6,10,2,6))
	print(sol.match(3,8,7,12))






