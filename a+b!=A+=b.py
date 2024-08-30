
a=10
print('a : ',a)
a=a+10
print(f'a+10 is {a}')
print('💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝')

a+=10
print(f'a+=10 is {a}')
print('💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝')

list1=[1,2,3]
list2=list1
list1+=list1
print(f'This is list1 (via list1+=list1){list1}')
print('💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝')
print(f'This is list2',list2)
print('💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝')

list3=[1,2,3]
list4=list3
list3=list3+list3
print(f'This is list (via list3+list3)',list3)
print('💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝💝')
print(f'this is list4',list4)
