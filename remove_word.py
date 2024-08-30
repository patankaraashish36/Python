def remove_word(text, word):
    words = text.split()
    print(words)
    filtered_words = [w for w in words if w != word]
    return ' '.join(filtered_words)

# Test the function
sentence = "This is a sample sentence with some words."
word_to_remove = "sample"
result = remove_word(sentence, word_to_remove)
print(result)  # Output: "This is a sentence with some words."
