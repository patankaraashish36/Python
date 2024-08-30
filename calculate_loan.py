
def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0
    
    if len(str(account_number)) != 4 or str(account_number)[0] != "1":
        print("Invalid account number")
    elif account_balance < 100000:
        print("Insufficient account balance")
    elif salary <= 25000 or loan_type.lower() not in ["car", "house", "business"] or loan_amount_expected < 1 or customer_emi_expected < 1:
        print("Invalid loan type or salary")
    elif (salary == 50000 and loan_type.lower() in ["house", "business"]) or (salary == 75000 and loan_type.lower() in ["business"]):
        print("Invalid loan type or salary") 
    else:
        if salary > 25000 and loan_type.lower() in ["car", "house", "business"]:
            if salary > 25000 and loan_type.lower() == "car":
                eligible_loan_amount = 500000
                bank_emi_expected = 36
            elif salary > 50000 and loan_type.lower() == "house":
                eligible_loan_amount = 6000000
                bank_emi_expected = 60
            elif salary > 75000 and loan_type.lower() == "business":
                eligible_loan_amount = 7500000
                bank_emi_expected = 84
            else:
                print("Invalid loan type or salary")
        if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected:
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:", customer_emi_expected)
        else:
            print("The customer is not eligible for the loan")
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
          

    #Use the below given print statements to display the output, in case of invalid data.
    #print("The customer is not eligible for the loan")
    
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"car",3000000,30)


