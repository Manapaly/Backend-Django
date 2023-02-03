class Bank:
    money: int 
    def __init__(self):
        self.money = 0
    def addToBankAccount(self, f):
        self.money += f

    def substractFromBankAcconunt(self, f):
        self.money -= f
    def moneyConversion(self, sum, a, b):
        if a == "USD" and b == "KZT":
            return sum * 470
        else:
            return sum/470
    def printSumOfBank(self):
        print(self.money)

b = Bank()
b.addToBankAccount(150)
b.printSumOfBank()
b.substractFromBankAcconunt(120)
b.printSumOfBank()

print(b.moneyConversion(300, "USD", "KZT"))

