# Create a BankAccount class that:
# 1. Has __init__ with account_holder, balance, account_type
# 2. Methods: deposit(), withdraw(), display_balance()
# 3. Validate withdrawal (balance check)
# 4. Track total deposits/withdrawals (class variable)

class bankaccount:
    Total_deposite=0
    Total_withdrawal=0
    
    def __init__(self,account_holder,balance,account_type):
        self.account_holder=account_holder
        self.balance=balance
        self.account_type=account_type

    def deposite(self,amount):
        if(amount<0):
            print("entered amount is invalid")
        else:
            self.balance += amount
            bankaccount.Total_deposite +=1
            print(f"you entered amount  deposites {amount}  account holder{self.account_holder}  balance is{self.balance}")


    def withdrawal(self,amount):
        if(amount<0):
            print("entered amount is not valid")
        
        elif(amount>self.balance):
            print("insufficient balance")

        else:
            self.balance-=amount
            bankaccount.Total_withdrawal+=1
            print(f"you entered a amount for withdrawal {amount} \n remaining balance{self.balance} \n account holder {self.account_holder}")    


    
    def bankbalance(self):
      print(f"the balance remaining in the account is {self.balance}")




acc1=bankaccount("hari",243526,"sbi")
acc1.deposite(92222)
acc1.withdrawal(90000)
acc1.bankbalance()