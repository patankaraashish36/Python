def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    dict={}
    data1=data.lower()
    list=data1.split()
    my_set=set(list)
    list2=[]
    for i in my_set:
        dict[i]=list.count(i)
        
    max=0
    
    for key,value in dict.items():
        if max<dict[key]:
            max=dict[key]
    #list3=[]
    list2=[]
    frequency=max
    for key,value in dict.items():
        if max==dict[key]:
            list2.append(key)
    
    word=list2[0]
    for i in range(1,len(list2)):
        if len(word)<len(list2[i]):
            word=list2[i]
    
    print(word,frequency)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)



def word_with_largest_frequency(text):
    # Convert all words to lowercase for case-insensitive comparison
    words = text.lower().split()

    # Create a dictionary to store word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Find the word(s) with the maximum frequency
    max_frequency = max(word_freq.values())
    max_frequency_words = [word for word, freq in word_freq.items() if freq == max_frequency]

    # If there are multiple words with the same frequency, choose the one with maximum length
    longest_word = max(max_frequency_words, key=len)

    return longest_word, max_frequency

# Test the function
text1 = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
result1 = word_with_largest_frequency(text1)
print(result1[0], result1[1])  # Output: like 3

text2 = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
result2 = word_with_largest_frequency(text2)
print(result2[0], result2[1])  # Output: fear 2
