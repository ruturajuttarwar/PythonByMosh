# #class

# class Student:     #class
#     #Default Constructor
#     college = "VIT"
#     name = "anon"  #class attribute
#     #Parameterized Constructor
#     def __init__(self, fullname, marks):
#         self.name = fullname   #obj attributes
#         self.marks = marks
#         print("New student Created")
    
#     def welcome(self):
#         print("Welcome", self.name)


# s1 = Student("Ruturaj", 87)  #object
# print(s1.name, s1.marks)  



# s2 = Student("Danny", 89)
# print(s2.college) 
# print(s2.welcome())
# print("Scored  " + str(s2.marks))


# class Car:
#     color = "Blue"
#     power = 1200
#     make = "German"
#     Air_Cool = True
#     Power_Str = True

# M1 = Car()
# if(M1.Air_Cool == True and M1.Power_Str == True):
#     print("Production Started")

# M2 = Car()


# class Student:
#     def __init__(self, Name, English_M, Math_M, Sci_M):
#         self.Name = Name
#         self.English_M = English_M
#         self.Math_M = Math_M
#         self.Sci_M = Sci_M

#     def Average(self):
#         Avg = (self.English_M + self.Math_M + self.Sci_M) / 3
#         return Avg


# s1 = Student("Ruturaj", 54, 67, 89)
# Avg = (s1.English_M + s1.Math_M + s1.Sci_M) / 3
# print(s1.Average())
        
# class Student:
#     def __init__(self, Name, Marks):
#         self.Name = Name
#         self.Marks = Marks

#     def Average(self):
#         sum = 0
#         for val in self.Marks:
#             sum += val
#         Avg = (sum / 3)
#         return Avg
    
#     @staticmethod
#     def Welcome():
#         return ("Welcome to Vit")


# s1 = Student("Ruturaj", [54, 67, 89])
# print(s1.Welcome())
# print(s1.Average())


# #Abstraction and encap
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clu = False

#     def start(self):
#         self.clu = True
#         self.acc = True
#         print("Car started")


# car1 = Car()
# car1.start()


# class Account:

#     @staticmethod
#     def Welcome():
#         return ("Welcome to the bank")

#     def __init__(self, balance, acc_num, acc_pass):
#         self.balance = balance
#         self.acc_num = acc_num
#         self.__acc_pass = acc_pass
        

#     def debit(self, amount):
#         if(self.balance > amount):
#             self.balance -= amount
#             print(str(amount) + " debited")
#             print("Updated balance = " + str(self.balance) )
#         else:
#             print("Insuff balance")

#     def credit(self, amount):
#             self.balance += amount
#             print(str(amount) + " credited")
#             print("Updated balance = " + str(self.balance) )


#     def Balance_check(self):
#          print("Balance = " + str(self.balance))

#     def Reset_pass(self, new_pass):
#          self.new_pass = new_pass
#          self.__acc_pass = new_pass
#          print(self.__acc_pass)

    
         
# e1 = Account(200, "13245", "abcde")
# e1.Balance_check()
# e1.credit(1000)
# e1.debit(50)
# e1.Balance_check()
# e1.Reset_pass("Rutur")

# #private
# class person:
#      __name = "abcd"

# p1 = person()

# print(p1.__name)


#Inheritance

class house:
    def __init__(self, owner, rent):
        self.owner = owner
        self.rent = rent

    @staticmethod
    def key():
        print("3 keys available")


class Villa(house):
    def __init__(self, name):
        self.name = name

    def floor(self):
        print("2 floor villa")


class VillaXL(Villa):
    def __init__(self, name):
        self.name = name



rental1 = VillaXL("Diplomat") 
rental1.floor()
rental1.key()


        
    


    
