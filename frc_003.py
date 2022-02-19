# find the first repeating character based on its alphabetical rank

# ex for string "y b a b c x y c y z x b y"
# here 'y' , 'b' are repeating. 'b' having lower alphabetical rank has higher precedance.
# first repeating character = b

# ex for string "x y z a b z b m n o "
# here 'z' , 'b' are repeating. 'b' having lower alphabetical rank has higher precedance.
# first repeating character = b

# ex for string "x y z a b a y z"
# here 'z', 'a', 'y' are repeating. 'a' having lower alphabetical rank has higher precedance.
# first repeating character = a

def frc(string_arr):
	# algorithm
	# make the count array while iterating the sting
	# iterate the count array if count of any char is >=2
	# convert index into char and print the char
	cnt = [0] * 26
	for ch in string_arr:
		cnt[ord(ch) - ord("a")] += 1
	for i in range(0, 26):
		if cnt[i] >= 2:
			return chr(i + ord("a")) 

if __name__ == '__main__':
	string_arr1 = "ybabcxycyzxby"
	string_arr2 = "xyzabzbmno"
	string_arr3 = "xyzabayz"
	print(frc(string_arr1))
	print(frc(string_arr2))
	print(frc(string_arr3))