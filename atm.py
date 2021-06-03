import random
balance = random.randint(100,10000)

class Atm:
    def __init__(self,card_number,pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self):
        print("Your balance is " + str(balance))

    def cash_withdrawl(self,amount):
        if(balance>=amount):
            new_amount = balance - amount
            print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
        else:
            print("You don't have enough money to withdrawl " + str(amount))

    def deposit_cash(self,deposit):
        cash_now = balance + deposit
        print("You have deposited amount " + str(deposit) + ". Your current balance is " + str(cash_now))


def main():
    card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Cash Withdrawl  3.Deposit Cash")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.cash_withdrawl(amount)
    elif (activity == 3):
        deposit = int(input("enter the amount:- "))
        new_user.deposit_cash(deposit)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()