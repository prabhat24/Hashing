

def largest_palindromic_string_m1(string):
	def check_palindrome(string, st, end):
		while st <= end:
			if string[st] != string[end]:
				return False
			st += 1
			end -= 1
		return True

	maxa = 0
	ans = ""
	st = 0
	end = 0
	for i in range(0, len(string)):
		for j in range(i, len(string)):
			if check_palindrome(string, i, j):
				if j-i +1 > maxa:
					maxa = j-i +1
					st = i
					end = j
	ans = string[st: end+1]
	return ans, maxa


def largest_palindromic_string_m2(string):

	def for_even(string, maxa, global_st, global_end):
		for i in range(0, len(string)-1):
			st = i
			end = i+1
			while st>=0 and end<len(string) and string[st] == string[end]:
				st -= 1
				end += 1
			if end - st -1  > maxa:
				global_end = end - 1
				global_st = st + 1
				maxa = global_end - global_st + 1
		return maxa, global_st, global_end 


	def for_odd(string, maxa, global_st, global_end):
		for i in range(0, len(string)):
			st = i
			end = i
			while st>=0 and end<len(string) and string[st] == string[end]:
				st -= 1
				end += 1
			if end - st - 1 > maxa:
				global_end = end - 1
				global_st = st + 1
				maxa = global_end - global_st + 1
		return maxa, global_st, global_end

	maxa, global_st, global_end = for_even(string, 0, 0, 0)
	maxa, global_st, global_end = for_odd(string, maxa, global_st, global_end)
	return string[global_st: global_end + 1], maxa



if __name__ == '__main__':
	string = "zdbabbabdzbaabcdy"
	print(largest_palindromic_string_m1(string))
	print(largest_palindromic_string_m2(string))


