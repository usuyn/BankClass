class BankAccount:
    count = 0
    __AccountNum = 1


    def __init__(self, name, money):
        self.customerName = name
        self.__accountNumber = BankAccount.__AccountNum
        self.money = money
        BankAccount.count += 1
        BankAccount.__AccountNum += 1

    def getName(self):
        return self.customerName

    def getBalance(self):
        return self.money

    def setBalance_add(self, amount):
        self.money += amount

    def setBalance_sub(self, amount):
        self.money -= amount

    def deposit(self, amount):
        self.setBalance_add(amount)
        print("입금완료\n")

    def withdraw(self, amount):
        if self.getBalance() < amount:
            print("잔액이 부족합니다.\n")
            return
        else:
            self.setBalance_sub(amount)
            print("출금완료", "\n")

    def transfer(self, acct, amount):
        if self.getBalance() < amount:
            print("잔액이 부족합니다.\n")
        else:
            self.setBalance_sub(amount)
            acct.setBalance_add(amount)
            print("이체완료\n")

    def show_acctInform(self):
        print("이름: ", self.getName())
        print("계좌번호: ", self.getAccountNum())
        print("잔액: ", self.getBalance(), "\n")

    @classmethod
    def getCount(cls):
        return cls.count

    def getAccountNum(self):
        return self.__accountNumber


class BankManager:
    acct = [] * 20
    cnt = 0

    def __init__(self, name, password):
        self.bankName = name
        self.__password = password

    def getBankName(self):
        return self.bankName

    def __getPassword(self):
        return self.__password

    @classmethod
    def create(cls):
        name = input("예금주명: ")
        money = int(input("초기 입금액: "))
        cls.acct.append(BankAccount(name, money))
        cls.cnt += 1
        print("계좌 생성이 완료되었습니다. \n")

    @classmethod
    def deposit(cls):
        print("[입금]")
        target = int(input("계좌번호: "))
        if cls.findAccount(target) < 0:
            print("계좌번호가 존재하지 않습니다.\n")
            return
        else:
            amount = int(input("입금액: "))
            cls.acct[target - 1].deposit(amount)

    @classmethod
    def withdraw(cls):
        print("[출금]")
        target = int(input("계좌번호: "))
        if cls.findAccount(target) < 0:
            print("계좌번호가 존재하지 않습니다.\n")
            return
        else:
            amount = int(input("출금액: "))
            cls.acct[target - 1].withdraw(amount)

    @classmethod
    def transfer(cls):
        print("[이체]")
        while True:
            acct1 = int(input("출금할 계좌: "))
            acct2 = int(input("입금할 계좌: "))
            if cls.findAccount(acct1) < 0 or cls.findAccount(acct2) < 0:
                print("계좌번호가 존재하지 않습니다. 다시 입력해주세요.")
                continue
            else:
                break
        amount = int(input("이체액: "))
        cls.acct[acct1 - 1].transfer(cls.acct[acct2 - 1], amount)

    @classmethod
    def findAccount(cls, target):
        for i in range(0, cls.cnt):
            if cls.acct[i].getAccountNum() == target:
                return i
        return -1

    def show_BankInform(self):
        print("지점명: ", self.getBankName())
        print("등록계좌 수: ", BankManager.cnt)
        choice = input("등록된 계좌의 정보를 보시겠습니까? y/n ")
        if choice == 'y':
            password = int(input("비밀번호 입력: "))
            if self.__getPassword() == password:
                print("\n------ 등록계좌 목록 ------")
                for i in range(BankManager.cnt):
                    BankManager.acct[i].show_acctInform()
            else:
                print("비밀번호 오류")
        elif choice == 'n':
            return
        else:
            return


def main():
    bank = BankManager("서울", 82635927)
    bank.create()
    bank.create()
    bank.create()
    bank.transfer()

    # git 연습용 수정
    bank.withdraw()
    bank.deposit()

    # # git branch 연습용
    # print("git branch practice")
    #
    # # git conflict 연습용
    # print("git conflict practice")

    bank.show_BankInform()

def user_UI():
    while True:
        bank = BankManager("서울", 720100)
        print("1.계좌개설 2.입금 3.출금 4.이체 5.종료")
        choice = int(input("실행할 작업의 숫자를 입력: "))
        if choice == 1:
            bank.create()
        elif choice == 2:
            bank.deposit()
        elif choice == 3:
            bank.withdraw()
        elif choice == 4:
            bank.transfer()
        elif choice == 5:
            return
        else:
            continue

if __name__ == "__main__":
    user_UI()