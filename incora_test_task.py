import random


class User:
    def __init__(self, name, money):
        pass


class SuperAdmin(User):
    def __init__(self, name, money):
        self.name = name

    def NewCasino():
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

    def getMoney():
        pass

    def takeMoney(number):
        pass



    def play(number):
        x = random.randint(100, 999)
        y = list(set(str(x)))
        if len(y) == 3:
            print(1)
        elif len(y) == 2:
            print(2)
        else:
            print(3)






