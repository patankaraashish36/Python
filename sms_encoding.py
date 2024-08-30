def sms_encoding(data):
    #start writing your code here
    data_list = data.split()
    vowel = "aeiouAEIOU"
    data = ""
    print(data_list)
    for w in data_list :
        if len(w) == 1:
                   data += w 
        else:
            for char in w:
                  if char not in vowel:
                     data += char 
        data +=" "
     
    return data[:-1]
                        
          
    
    # return data
data="I love Python"
print(sms_encoding(data))