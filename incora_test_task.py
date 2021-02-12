import random


class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money > 0  # it will not work, find the answer
        self.gameMachine = []

    def play(self, money):
        pass


class Casino:
    def __init__(self, name):
        self.name = name

    def getMoney():
        pass

    def getMachineCount():
        pass


class GameMachine:
    def __init__(self, number):
        self.number = number

    def getMoney(self):
        pass

    def takeMoney(self, number):
        pass

    def putMoney(self, number):
        pass

    def play(self, number):
        x = random.randint(100, 999)
        y = list(set(str(x)))
        if len(y) == 3:
            return number
        elif len(y) == 2:
            return number * 2
        else:
            return number * 3


class SuperAdmin(User):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.casino = []
        self.gameMachine = []

    def NewCasino(self, name):
        self.casino.append(Casino(name))

    def NewGameMachine(self, idNumber):
        self.gameMachine.append(GameMachine(money))

