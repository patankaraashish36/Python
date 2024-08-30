from collections import counter 
with open("example.txt" ,"r") as file:
    content = file.read()
    words = content.split()
    word_count = counter(words)
    top_words = word_count.most_common(10)
    
    for word , count in top_words:
        print(f"{word} : {count}")