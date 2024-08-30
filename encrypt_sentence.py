def encrypt_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty list to store the encrypted words
    encrypted_words = []

    # Iterate through the words with their indices
    for i, word in enumerate(words, 1):
        # If the index is odd, reverse the word
        if i % 2 != 0:
            encrypted_words.append(word[::-1])
        else:
            # Rearrange the word with consonants before vowels
            consonants = [char for char in word if char.lower() not in 'aeiou']
            vowels = [char for char in word if char.lower() in 'aeiou']
            rearranged_word = ''.join(consonants + vowels)
            encrypted_words.append(rearranged_word)

    # Join the encrypted words back into a sentence
    encrypted_sentence = ' '.join(encrypted_words)

    return encrypted_sentence

# Test the function
sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print("Encrypted Sentence:", encrypted_sentence)
