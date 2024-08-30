child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
# print(child_id.index(20))
def calculate_total_chocolates():
    total_chocolates = 0
    for i in chocolates_received:
        total_chocolates  = i + total_chocolates
    return total_chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded in child_id :
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
        else:
            index = child_id.index(child_id_rewarded)
            chocolates_received[index] = chocolates_received[index] + extra_chocolates
            print(chocolates_received)
    else:
        print("Child id is invalid")
    
# print("Extra chocolates is less than 1")
# print("Child id is invalid")
# print(chocolates_received)
print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)