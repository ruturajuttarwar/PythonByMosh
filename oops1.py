# from oops import Account
# from oops import e1
# e1.Balance_check()
# e1.credit(1000)
# e1.debit(50)
# e1.Balance_check()

# del e1



records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
    
sorted_grades = sorted(set(grade for name, grade in records))
second_lowest_grade = sorted_grades[1]
second_lowest_students = [name for name, grade in records if grade == second_lowest_grade]
second_lowest_students.sort()

for student in second_lowest_students:
    print(student)
    
    
            
            
            
      