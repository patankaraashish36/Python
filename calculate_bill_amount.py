def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    first_3kms_charge = 0
    next_3kms_charge = 3
    remaining_charge = 6

    if food_type in ["N" ,"n"]:
        if distance_in_kms <= 3:
            bill_amount =   150 * quantity_ordered + first_3kms_charge
        elif distance_in_kms <= 6:
            bill_amount =  150 * quantity_ordered + first_3kms_charge + next_3kms_charge * (distance_in_kms - 3)
        else:
            bill_amount = 150 * quantity_ordered + first_3kms_charge + next_3kms_charge * 3 + remaining_charge * (distance_in_kms - 6)
    else:
        if distance_in_kms <= 3:
            bill_amount =   120 * quantity_ordered + first_3kms_charge
        elif distance_in_kms <= 6:
            bill_amount =  120 * quantity_ordered + first_3kms_charge + next_3kms_charge * (distance_in_kms - 3)
        else:
            bill_amount = 120 * quantity_ordered + first_3kms_charge + next_3kms_charge *3 + remaining_charge * (distance_in_kms - 6)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("n",2,8)
print(bill_amount)



print("-"*50)

#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    first_3kms_charge = 0
    next_3kms_charge = 3
    remaining_charge = 6

    if food_type not in ["N","V"] or quantity_ordered < 1 or distance_in_kms <= 0:
        return -1

    if food_type == "N":
        item_price = 150
    elif food_type == "V" :
        item_price = 120

    if distance_in_kms <= 3:
        bill_amount = item_price * quantity_ordered + first_3kms_charge
    elif distance_in_kms <= 6:
        bill_amount = item_price * quantity_ordered + first_3kms_charge + next_3kms_charge * (distance_in_kms - 3)
    else:
        bill_amount = item_price * quantity_ordered + first_3kms_charge + next_3kms_charge * 3 + remaining_charge * (
                    distance_in_kms - 6)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)