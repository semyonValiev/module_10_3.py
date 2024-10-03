from random import randint
from time import sleep
from threading import Thread, Lock

class Bank:

    def __init__(self, lock = None , balance = 0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            cash = randint(50, 500)
            self.balance += cash
            print(f'Пополнение баланса на {cash}, Текущий баланс {self.balance}руб.')
            sleep(0.01)

    def take(self):
        for i in range(100):
            cashback = randint(50, 500)
            print(f'Запрос на вывод {cashback}')
            if cashback > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= cashback
                print(f'снятие {cashback} прошло успешно, баланс {self.balance}')

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')