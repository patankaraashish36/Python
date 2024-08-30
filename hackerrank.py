def miniMaxSum(arr):
    total1=0
    total2=0
    s=sorted(arr)
    print(s)
    # length = len(arr)
    # l= length -1
    maximum=s[1:]  # 2,7,69,221,8974
    minimum=s[0:5]
    for i in range(0,len(maximum)):
        total2 = total2 + maximum[i]
        total1= total1 + minimum[i]
    print(total1 , total2)
miniMaxSum([1,3,5,7,9])


s="ssddffgg"
print(s[:-2])


def is_leap(year):
    leap = False
    
    if (year % 400 == 0) and (year % 100 == 0):
      return leap
    elif (year %4 == 0) or (year % 100 != 0):
      return leap
    
print(is_leap(1990))