def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return -1
        arr = []
    n = int(input("enter element : "))
    for i in range(n):
        num = float(input("enter element ", + str(i+1) + " : "))
        arr.append(num)

        x= float(input("search element : "))
        result = linear_search(arr,x)
        if result ==1 :
            print(False)
        else:
            print(True, result)