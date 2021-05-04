#classAccount.py
#Account class that mimics a bank account. Has a balance, name, and account number
#and has methods to deposit, withdraw, and report balance.
#by S. Allen


class Account:

    def __init__(self, name, number, balance):
        self.balance = float(balance)
        self.name = name
        self.number = number

#   #getters
    def getBal(self):
        return self.balance

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    
#   #actions
    def deposit(self, money):
        self.balance += float(money)    

    def withdraw(self, money):
        self.balance = self.balance - float(money)

    def chname(self, newname):
        self.name = newname
        

def main():
    print('Creating an account for Joe as the first account, with an inital deposit of $45.','\n')
    
    myaccount = Account('Joe', 1, 45)

    print('Joe decides to deposit $5 into his account.')
    myaccount.deposit(5)

    print('His new balance is $',myaccount.getBal(),'dollars.','\n')

    print('Joe wants to change his name to Jane.')
    myaccount.chname('Jane')

    print('His account name is updated to say:',myaccount.getName(),'\n')

    print('Jane decides to withdraw $10 from his account.')
    myaccount.withdraw(10)

    print('His new balance is $',myaccount.getBal(),'dollars.','\n')

    acclist = []
    namelist = ['sarah', 'matt', 'kali', 'laura', 'ed']
    
    
    for i in range(5):

        myaccount = Account(namelist[i], 1, 45)
        acclist.append(myaccount)

    for x in acclist:
        print('This account belongs to: ', x.getName())
        
    print(acclist[2].getName())        
        


main()
    
    

    

    
