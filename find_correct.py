def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    worng = 0
    for key,value in word_dict.items():
        # print(key,value)
        if key == value:
            correct +=1
        else:
            diff_count = sum([1 for w1 , w2 in zip(key,value) if w1 != w2 ])
            if diff_count <=2:
                almost_correct += 1
            else:
                worng +=1

    return [correct ,almost_correct, worng] 

word_dict ={'CHECK': 'CHEK', 'RADIO': 'RADICAL', 'MIND': 'MUND', 'VENDOR': 'VENDING', 'ALWAYS': 'ALWAYSE', 'ALWAYS': 'ALWAYS'}
print(find_correct(word_dict))





print("-"*50)

print("Comparation upto equal length")

def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    worng = 0
    for key,value in word_dict.items():
        # print(key,value)
        if key == value:
            correct +=1
        elif (len(key) == len(value)):
            diff_count = sum([1 for w1 , w2 in zip(key,value) if w1 != w2 ])
            if diff_count <=2:
                almost_correct += 1
            else:
                worng +=1
        else: 
            worng +=1
    return [correct ,almost_correct, worng] 

word_dict ={'CHECK': 'CHEK', 'RADIO': 'RADICAL', 'MIND': 'MUND', 'VENDOR': 'VENDING', 'ALWAYS': 'ALWAYSE', 'ALWAYS': 'ALWAYS'}
print(find_correct(word_dict))