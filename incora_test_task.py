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

    def unique(list1):     
        unique_list = []
        for x in list1:
        
            if x not in unique_list:
                unique_list.append(x)
   

    def play(number):
        x = random.randint(100, 999)

        y = list(str(x))
        print(y)

        
# def unique(y): 
#     unique_list = []
#     for x in y:                
#         if x not in unique_list:
#             unique_list.append(x)
#     # for x in unique_list:
#     #     print(x)
#     if unique_list 
    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# x = random.randint(100, 999)
# y = list(str(x))
# unique(y)
# print(y)