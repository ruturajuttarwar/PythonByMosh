# first_name = "Ruturaj"
# last_name = "Uttarwar"
# age = 30
# is_new = False
# print(first_name,last_name)
# print(age)
# if(is_new):
#     print("New patient")
# else:
#     print("Already registered")

# Name = input("Name? ")
# print("Hello " + Name)


#convert type to type
# year = input("Enter birth year ")
# age = 2025 - int(year)
# print(age)

# #Type conversion
# print("Calculator")
# first_num = input("Enter first number)")
# second_num = input("Enter second number")
# Sum = print("Sum is " + str(float(first_num) + float(second_num)))

# #strings
# course = "Python for Begineers"
# print(course.upper())
# print(course.lower())
# print(course.find("e"))
# print(course.replace("e", "t"))
# print("Pyhon" in course)
# print(course)

# #Arthimatic operators
# x = 20
# x += 3
# print(x)

# print(10 // 3)
# print(10 / 3)
# print(10 % 3)

# #Operator prescendance
# x = 10 + 3 * 2
# print(x)

# #Comparision Operator
# x = 3 > 2
# x = 3 < 2
# x = 3 >= 2
# x = 3 <= 2
# x = 3 == 2
# x = 3 != 2
# print(x)


# #Logical Operators
# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)


# #If statements
# temp = 12
# if temp > 30:
#     print("It's a hot day")
#     print("Drink water")
# elif temp > 20:
#     print("It's a nice day")
# elif temp > 10:
#     print("Its a bit cold")
# else:
#     print("Its cold")
# print("done")



# # Exercise
# weight = float(input("Weight: "))
# choice = input("(K)g or (L)bs: ")
# if(choice == 'K' or choice == 'k'):
#     convert = weight * 2.20
#     print("Weight is " + str(convert) + " Lbs")
# elif(choice == 'L' or choice == 'l'):
#     convert = weight * 0.45
#     print("Weight is " + str(convert) + " Kgs")

# #While loops
# i = int(input("Enter number"))
# n = 1
# while(n <= i):
#     print(n * '*')
#     n += 1


# #Lists
# names = ["john", "Bob", "Mosh", "Sam", "Mary"]
# print(names[3:5])
# print(names[-3:-1])
# print(names[-1])
# names[0] = "jon"
# print(names)
# print(names[0:3])


# #List methods
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(8)
# numbers.insert(2, 5)
# numbers.remove(4)
# #numbers.clear()
# print(numbers)
# print(len(numbers))


# #For loops
# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#      print(i)
# i = 0
# print(" ")
# while(i < len(numbers)):
#     print(numbers[i])
#     i += 1


# #Range Function
# numbers = range(5, 10, 2)
# for number in numbers:
#     print(number)

# for number in range(0, 100, 2):
#     print(number)

#Tuples
numbers = (1, 2, 3, 4, 5, 6)
#numbers[0] = 3
count = numbers.count(3)
print(count)