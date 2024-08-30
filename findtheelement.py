l=[1,4,6,8,0,3]
a=int(input("Enter the element whoose you find. :"))
if a in l:
    print(f"yes element present at index {l.index(a)}") 
else:
    print('Element is not present.')