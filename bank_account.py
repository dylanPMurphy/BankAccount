class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate #must be less than 1
        self.balance = balance



    # deposit(self, amount) - increases the account balance by the given amount

    def deposit(self, amnt):
        self.balance+=amnt
        return  self
    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdraw(self, amnt):
        self.balance-=amnt
        return  self
    # display_account_info(self) - print to the console: eg. "Balance: $100"

    def displayAccontInfo(self):
        print("Current Balance:" + str(self.balance) + " ---Current interest rate: "+str(self.int_rate))
        return  self


    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

    def yeildInterest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance*self.int_rate
        return self


def testCases():
    ba01 = BankAccount(324123.23,.03)
    ba01.displayAccontInfo()