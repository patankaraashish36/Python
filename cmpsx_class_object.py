class Atm:
    def __init__(self) -> None:
        self.pin = ""
        self.balance = 0
        self.manu()
    def manu(self):
        print("""
            1. Press 1 for Create PIN.
            2. Press 2 for Change PIN.
            3. Press 3 for Check Balance. 
            4. Press 4 for Withdraw
            5. Press Anything to exit.
            """)
        user_input = int(input("Enter number in between 1 to 4. : "))
        if user_input == 1:
            # create PIN
            self.create_pin()
            self.manu()
        elif user_input == 2:
            # change PIN
            self.change_pin()
            self.manu()
        elif user_input == 3:
            # Check Balance
            self.check_balance()
            self.manu()
        elif user_input == 4:
            # Withdraw
            self.withdraw_balance()
            self.manu()
        else:
            exit()
    
    def create_pin(self):
        set_pin = int(input("Enter 4 Number PIN. : ")) 
        print(len(str(set_pin)))
        if len(str(set_pin)) == 4:
            self.pin = int(set_pin)
            self.balance = int(input("Enter your Bank Balance. : "))
        else:
            print("Bewakuf itna bhi nhi malum fix 4 anko ka hota hy ATM PIN, chal nikal yaha se.")

    def change_pin(self):
        user_pin = int(input("Enter 4 Number currunt PIN. : "))
        if user_pin == self.pin:
            new_pin =  int(input("Enter new PIN. : "))
            self.pin = new_pin
            print("PIN set successfully.")
        else:
            print("Bewakuf meri tarah hy kya tu bhi PIN bhul jata hyy or 4 Number ka dal. ")

    def check_balance(self):
        user_pin = int(input("Enter 4 Number PIN. : "))
        if user_pin == self.pin:
            print(self.balance)
        else:
            print("Bewakuf meri tarah hy kya tu bhi PIN bhul jata hyy or 4 Number ka dal.")

    def withdraw_balance(self):
        user_pin = int(input("Enter 4 Number PIN. : "))
        if user_pin == self.pin:
            wtw_balance = int(input("Enter balance you want to withdraw. : "))
            if wtw_balance <= self.balance:
                self.balance = self.balance - wtw_balance
                print("Please collect cash - ", wtw_balance)
                print("Remaining Balance - ", self.balance)
            else:
                print("Jyda uper ud raha hyy, ground pe aa ground pe, samjhe.")
        else:
            print("Bewakuf meri tarah hy kya tu bhi PIN bhul jata hyy or 4 Number ka dal.")



        
    
    
p1 = Atm()