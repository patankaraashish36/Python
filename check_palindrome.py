def check_palindrome(word):
   if word[::-1] == word:
       return True
   else:
       return False 

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")

# x = "helo"
# y = x[::-1]
# print(y)