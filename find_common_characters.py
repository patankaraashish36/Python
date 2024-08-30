# def find_common_characters(msg1,msg2):
#     new_msg = ""
#     if msg1 != msg2 :
#         for char in msg1:
#             if char in msg2:
#                 new_msg = new_msg + char
#     else:
#         pass
#     if not new_msg:
#         return -1
#     else:
#         return new_msg.replace(" ","")
# #Provide different values for msg1,msg2 and test your program
# msg1="moto"
# msg2="moto"
# common_characters=find_common_characters(msg1,msg2)
# print(common_characters)




def find_common_characters(msg1,msg2):
    m1 = msg1.replace(" ","")
    m2 = msg2.replace(" ","")
    l = []
    s = []
    for  i in m1:
        if i in m2:
            l.append(i)
    for a in l:
        if a not in s:
            s.append(a)

    if len(s)>0:
        return "".join(s)
    else:
        return -1


#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)