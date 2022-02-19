# find the first repeating character based on its index of last occurance

# ex for string "y b a b c x y c y z x b y"
# first repeating character = b 

# ex for string "x y z a b z b m n o "
# first repeating character = z

# ex for string "x y z a b a y z"
# first repeating character = a

def frc(string_arr):
	# algorithm
	# make the count array while iterating the sting
	# while iterating, if count of any character becomes >=2, print that char.
	cnt = [0] * 26
	for ch in string_arr:
		cnt[ord(ch) - ord("a")] += 1
		if cnt[ord(ch) - ord("a")] >= 2:
			return ch 

if __name__ == '__main__':
	string_arr1 = "ybabcxycyzxby"
	string_arr2 = "xyzabzbmno"
	string_arr3 = "xyzabayz"
	print(frc(string_arr1))
	print(frc(string_arr2))
	print(frc(string_arr3))