def func(sample, res, key,val):
    index =- 1
    if(key in sample):
        res = True
        index = sample.index(key)
        values[index] = val
    else:
        res = False
    return index

res = None
sample = ["A","B","C","D"]
values = [1,1,3,4,5]
index = func(sample,res,"B",2)
print(values[index], res)

print("-"*50)


def func1(arg1,arg2 = 5):
    if(arg1 > arg2):
        return arg1
    return arg2
def func2(arg3,*arg4):
    for i in arg4:
        if(arg3 == i):
            return i
    return 0
def func3(arg5,arg6):
    if(arg5 == arg6):
        return True
    return False
res1 = func1(1)
res2 = func2(res1,1,1,2,5,7,8)
print(func3(arg6 = 5,arg5 = res2))
 

print("-"*50)

def find_avg(list_num):
    result_sum=0
    for num in list_num:
        result_sum+=num
    result_avg=result_sum/len(list_num)
find_avg([5,8,5])
print(result_avg)

