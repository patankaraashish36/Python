# print("1a".isalnum())
# print(int("011"))
def solve(s):
    if s.isalnum():
        return s
    else:
        s = s.title()
        return s
print(solve("1 w 2 r 3g"))
print("1 w 2 r 3g".isnumeric())


print({1,2,[1,2]})


# def validAbbreviation (str, abbr):
# 	# Write your code here.
# 	i = 0
# 	j=0
# 	result = None
# 	digit = "0"
# 	len_abbr = len(abbr)
# 	while len_abbr >= 0:
# 		if abbr[i].isalpha():
# 			if str[i] == abbr[i+j]:
# 				result = True
# 			else:
# 				result = False
# 				break

# 		if abbr[i].isdigit:
# 			if abbr[i+1].isdigit:
# 				digit += abbr[i]
# 			digit += abbr[i]
# 		else:
# 			digit = "0"

# 			i = i+1
# 			j = j+ int(digit)
# 			len_abb -= 1
# 	return result


# print(validAbbreviation("abbreviations", "a11s"))