# writting to a file
l= " Aashish Patankar"
# with open("aashish.txt","w") as a:
#     a.write(l)


#old method
# s= open("aashish.txt","w")
# s.write(l)


# Reading to a file

with open("aashish.txt","r") as a:
    p=a.read()
    print(p)

# Appending to a file


with open("aashish.txt","a") as a:
    a.write(l)