
class Solution():

	P = 2
	k = 1<<31 -1

	def preprocess_power(self, m):
		self.power = [1] * (m + 1)
		pow = 1
		for i in range(1, m+1):
			self.power[i] = (self.power[i-1] * self.P) % self.k

	def get_pattern_hash(self, pattern, m):
		hp = 0
		for i in range(m):
			hp =  (hp + ((ord(pattern[i]) - ord('A')) * self.power[m-i]) % self.k) % self.k
		return hp

	def match_string(self, string, pattern, n, m):
		self.preprocess_power(m)
		hp = self.get_pattern_hash(pattern, m)
		hs = 0
		for i in range(m):
			hs =  (hs + ((ord(string[i]) - ord('A')) * self.power[m-i]) % self.k) % self.k
		if hs == hp:
			return True, 0

		for i in range(m, n):
			# hs = ((((hs - ord(string[i-m]) - ord('A')) * self.power[m]) * self.P) + (ord(string[i-m]) - ord('A')) * self.P) % self.k

			remove_old_hash = ( hs - ((ord(string[i-m]) - ord('A')) * self.power[m]) % self.k + self.k ) % self.k
			shift_hash = (remove_old_hash * self.P) % self.k
			new_term = (ord(string[i]) - ord('A')) * self.P
			hs = (shift_hash + new_term) % self.k
			if hs == hp:
				return True, i - m + 1
		return False, n+1

if __name__ == "__main__":
	string = "dsfmfassssmtsfmtfsxyfgssamtas"
	pattern = "samtas"
	sol = Solution().match_string(string, pattern, len(string), len(pattern))
	print(sol)
