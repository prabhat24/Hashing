# find the first repeating character based on its index on first occurance.

# ex for string "y b a b c x y c y z x b y"
# first repeating character = y 

# ex for string "x y z a b z b m n o "
# first repeating character = z

# ex for string "x y z a b a y z"
# first repeating character = y

def frc(string_arr):
	# algorithm
	# make the count array while iterating the sting
	# again iterate the sting look at the count of each char
	# print the char if its count >= 2
	cnt = [0] * 26
	for ch in string_arr:
		cnt[ord(ch) - ord("a")] += 1
	for ch in string_arr:
		if cnt[ord(ch) - ord("a")] >= 2:
			return ch 

if __name__ == '__main__':
	string_arr1 = "ybabcxycyzxby"
	string_arr2 = "xyzabzbmno"
	string_arr3 = "xyzabayz"
	print(frc(string_arr1))
	print(frc(string_arr2))
	print(frc(string_arr3))