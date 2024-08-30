list_of_marks=(24, 24, 24, 24, 24, 24, 24, 25, 24, 24)
avg_marks = sum(list_of_marks) // len(list_of_marks)

def find_more_than_average():
    count = 0
    for makrs in list_of_marks:
        if makrs > avg_marks:
            count +=1
    percentage = (count / len(list_of_marks)) * 100
    return percentage
def sort_marks():
     sort = sorted(list_of_marks)
     return sort
def generate_frequency():
    # count = []
    # for mark in range(26):
    #         if list_of_marks.count(mark)>1:
    #              count.append(list_of_marks.count(mark))
    #         elif mark in list_of_marks:
    #             count.append(1)
                                 
    #         else:
    #             count.append(0)
    # return count
    frequency = [0]*26  
    for marks in list_of_marks:
        frequency[marks] += 1
    return frequency
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())


