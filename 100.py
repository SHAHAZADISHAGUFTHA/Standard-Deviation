import random

class atm(object):
    def __init__(self,CardNumber, pin):
        self.CardNumber = CardNumber
        self.pin = pin

    def cashWithdrawl(self,CardNumber, pin):
        amount = int(input("Enter the amount you want to withdraw: "))
        print("The amount Rs. " + str(amount) + " has been withdrawn from Card number: " + str(CardNumber) + " and pin: " + str(pin))

    def checkBalance(self,CardNumber, pin):
        balance = 50000
        print("You currently have Rs. " + str(balance) + " in Card number: " + str(CardNumber) + " and pin: " + str(pin))


print("Press 111 for withdrawing cash\nPress 112 for balance enquiry")
action = input("Enter your action: ")

ATM = atm(15, 20)
if action == "111":
    ATM.cashWithdrawl(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))
elif action == "112":
    ATM.checkBalance(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))

   