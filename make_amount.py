#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=min(rupees_to_make//5, no_of_five)
    one_needed=0

    remain_rupees = rupees_to_make -(five_needed*5)
    if remain_rupees > no_of_one:
        print(-1)
    else:
        one_needed = remain_rupees

        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your progr
(make_amount(21,5,3))
