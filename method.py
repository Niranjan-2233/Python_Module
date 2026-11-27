'''
name="Niranjan Somnath Waman"
print(name.upper()) #NIRANJAN SOMNATH WAMAN
print(name.lower()) #niranjan somnath waman

institude="the kiran academy"
print(institude.title()) #The Kiran Academy
print(institude.capitalize()) #The kiran academy

password="Niranjan 12"
print(password.isalpha())
print(password.isalnum())
print(password.title())
print(password.isupper())
print(password.isspace())
print(password.replace("12","11"))
print(password.index("a",4))

name="python,is,programming,language"
print(name.index("n",5))#"n" means that which char. want to find and 5 means from which index whant to start
print(name.count("n"))# .count() cout the number of spacific character in string  
print(name.count("a",10,-9))# 10 is start index and -9 is end index
print(name.split())
print(name.split(","))
'''
# name="Niranjan waman"
# name1="    Niranjan waman     "
# print(name)
# print(name1.strip())
# print(name.rstrip("n"))
# print(name.lstrip("N"))

# name="Niranjan","waman"
# print(name.startswith("M"))#False
# print(name.endswith("n"))#True
# print(" ".join(name))
# print(name.center(23,"-"))

# name=["nirajan","somnath","waman"]
# full_n=" ".join(name)
# print(full_n)

# name="Nirajan"
# for char in name:
#     print(char)

# name="Rahul manohar raut"
# name1=name.split()
# for char in name1:
#     print(char)

course="data analytic,data science,web devlopment,testing"
s=course.split(",")
for i in s:
    print(i)
    
