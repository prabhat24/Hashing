def preprocessing(str_array):
	arr_hash = []
	for string in str_array:
		_hash = [0] * 26
		for ch in string:
			_hash[ord(ch) - ord('a')] += 1
		arr_hash.append(_hash)
	return arr_hash

def check_if_anagrams(i, j, arr_hash):
	for k in range(0, 26):
		if arr_hash[i][k] != arr_hash[j][k]:
			return False
	return True

def count_anagramic_groups_m1(str_array):
	# algorithm
	# 1. create the count arrays of each of the string.
	# 2. take 2 pointer and create all possible pairs.
	# 3. check if the 2 strings are anagrams

	# Suppose N is length of str_array and m is avg length of the strings in the string array
	# complexity
	# time - N^2 * (M+26) | space - 1 [if prerocessing of count array is not done] 
	# time - N*m + N^2 * (26) | space - N*26 [if prerocessing of count array is not done] 
	arr_hash = preprocessing(str_array)
	groups = []
	for i in range(0, len(str_array)):
		if str_array[i] is None:
			continue
		anagram_grp = [i,]
		for j in range(i+1, len(str_array)):
			if check_if_anagrams(i, j, arr_hash):
				anagram_grp.append(j)
		groups.append(anagram_grp)
		for k in anagram_grp:
			str_array[k] = None
	# print(groups)
	return len(groups)


def count_anagramic_groups_m2(str_array):
	# algorithm
	# 1. iterate all the strings in str_array
	# 1. sort string (m)
	# 2. put sorted strings into a set  (m)
	# complexity
	# time N*(m + m)| space-N*m (for set)

	def count_sort(string):
		cnt = [0] * 26
		for ch in string:
			cnt[ord(ch) - ord('a')] += 1
		srt_str = ""
		for i in range(0, 26):
			for j in range(0, cnt[i]):
				srt_str = srt_str + chr(i+ord('a'))
		return srt_str

	groups = set()
	for string in str_array:
		srt_str = count_sort(string)
		groups.add(srt_str)
	print(groups)
	return len(groups)


if __name__ == '__main__':
	str_array = ['east', 'seat', 'ate', 'eat', 'abca', 'bacb', 'abcac', 'abacd', 'bcba', 'bbca', 'aacb', 'baac']
	# print(count_anagramic_groups_m1(str_array))
	print(count_anagramic_groups_m2(str_array))