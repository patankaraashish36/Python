list_of_airlines=["AI","EM","BA"]

print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])

print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)
    
print("Using while loop")
i = 0
while (i < len(list_of_airlines)):
    print(list_of_airlines[i])
    i = i+1

my_list = [1, 2, 3, 4, 5]
index = -1
while abs(index) <= len(my_list):
    print(my_list[index])
    # print(index)
    index -= 1
for i in range(-1,-6,-1):
    print(my_list[i])

my_list = [1, 2, 3, 4, 5]
while my_list:
    print(my_list[0])
    break
