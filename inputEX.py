# course=input("Enter course name= ")
# print(f"course name is {course}")

# name=str(input("Enter account holder name= "))
# acc_number=int(input("Enter account number= "))
# print(f"Accound holder = {name} \nAccount number = {acc_number}")


# num=int(input("Enter number :"))
# square=num**2
# print(f"The square of {num} is {square}")
'''
# type casting
num=199
print(type(num)) #<class 'int'>
int=float(num)
print(type(int)) #<class 'float'>

#Example 2
a="44"
print(type(a)) #<class 'str'>
str=int(a)
print(type(str)) #<class 'int'>
'''

# name=input("Enter customer Name= ")
# P_amount=int(input("Enter principal amount= "))
# R_intrest=int(input("Enter rate of intreat= "))
# Time_period=int(input("Enter time period in yerars= "))
# simple_interst=(P_amount*R_intrest*Time_period)/100
# print(f'''
# Name = {name}
# Principal amount = {P_amount}
# Rate of intreat={R_intrest}
# Time in years = {Time_period}
# simple intrest is {simple_interst}
# ''')

name=input("Enter customer Name= ")
roll=int(input("Enter roll no= "))
course=input("Course name= ")
total_fee=int(input("Enter total fee= "))
adm_fee=int(input("Adimission fees= "))
exam=int(input("Examination fees= "))
discount=int(input("Discount= "))
Amout=int(input("Amount payed= "))
discount_c=total_fee-total_fee*discount/100
print(f'''
name of student= {name}
Roll number={roll}
course = {course}
total fees= {total_fee}
Adimission fees={adm_fee}
Exam fees= {exam}
Discount in perctage= {discount}
Amount payed= {Amout}
Course after discount= {discount_c}
''')