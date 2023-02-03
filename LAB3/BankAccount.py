import enum
class WalletType(enum.Enum):
    KZT = "KZT"
    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"

WalletTypes = [(member.name, member.value) for member in WalletType]

class BankAccount:
    name: str
    surname: str
    _deposit: float
    account: WalletType
    def __init__(self, name: str, surname: str, account: WalletType):
        self.name = name
        self.surname = surname
        self.account = account
        self.deposit = 0
    def addToBankAccount(self, f: float):
        self.deposit += f
    def substractFromBankAcconunt(self, f: float):
        self.deposit -= f
    def getDeposit(self):
        return self.deposit
    def setDeposit(self, sum: float):
        self.deposit = sum
    def toString(self):
        return self.name + " " + self.surname + " with " + self.account[0] + " type"
    # def __del__(self):
    #     print(f'Object {self.name} destroyed!')
    def __str__(self):
        print(f'{self.name} + " created!')

dataBase = []
# print(WalletTypes)

def menu():
    print("Выберите ваше действие:\n1. Создание пользователя \n2. Выбрать пользователя \n0. Выйти")
    a = int(input())
    if(a == 1):
        print("Введите имя пользователя: ")
        name = input()
        print("Введите фамилию пользователя:")
        surname = input()
        print("Выберите тип кошелка: " + "[1/" + str(len(WalletTypes)) + "]")
        ind = 1
        for i in WalletTypes:
            print(str(ind) + ": " + str(i[1]))
            ind += 1
        chAcc = int(input())
        dataBase.append(BankAccount(name, surname, WalletTypes[chAcc - 1]))
        # print(dataBase[0].toString())




menu()
# print(dataBase)