
# name=(input("Enter costumer name: "))
# product=(input("Enter product name: "))
# price_item=int(input("Enter price per item: "))
# quantity=int(input("Quantity purches: "))
# discount_persentage=int(input("Discount in persentage: "))
# before_d=price_item*quantity
# discount=price_item*discount_persentage/100
# gst=discount*18/100
# total=discount+gst
# print(f'''
# Name of customer = {name}
# Product name = {product}
# Price of product = {price_item}
# Quantity = {quantity}
# total bill = {before_d}
# Discount amount = {discount_persentage}
# After discount = {discount}
# GST 18% ={gst}
# final bill = {total}
# ''')

# name=input("Enter customer name= ")
# Hotel_name=("Enter Hotel name= ")
# no_room=int(input("Enter number of room = "))
# price_room=int(input("Price per room per night = "))
# No_night=int(input("Enter number of night= "))
# discount_percentage=int(input("Discount= "))
# total=no_room*price_room
# discount=total*discount_percentage/100
# after_discount=total-discount
# service=after_discount*5/100
# final_amount=after_discount+service
# print(f'''
# Name of customer= {name}
# Name of hotel = {Hotel_name}
# number of rooms book= {no_room}
# Price per room per night= {price_room}
# NUMBER OF NIGHT = {No_night}
# discount percentage= {discount_percentage}
# Total = {total}
# discount amount= {discount}
# after discount= {after_discount}
# Service charges ={service}
# Final amount to pay= {final_amount}''')



# name=input("Enter customer name= ")
# car=input("Enter car model= ")
# rantal_day=int(input("Number of rantal days= "))
# daily_charge=int(input("daily rental charges= "))
# Total_km=float(input("Total kilomiter drive= "))
# Charge_km=float(input("Charge per kilometer= "))
# total=rantal_day*daily_charge
# travling_charge=Total_km*Charge_km
# subtotal=total+travling_charge
# gst=subtotal*18/100
# final_pay=subtotal+gst
# print(f'''
# Name of customer= {name}
# Car model = {car}
# Number of rental days= {rantal_day}
# Daily reantal charges = {daily_charge}
# Total kilomiter drive = {Total_km}
# Charge per kilometer = {Charge_km}
# Total rant = {total}
# Travilling charges based on KM = {travling_charge}
# Subtotal = {subtotal}
# GST Amount (18%)= {gst}
# Final amount to pay = {final_pay}
# ''')


name= input("Enter employee name= ")
Employee_id=("Enter employee ID = ")
travelling_days=int(input("Enetr the travelling days = "))
daily_food=int(input("Daily food allowance = "))
Hotel_charge=int(input("Hotel charges per night = "))
ticket_cost=int(input("Total travilling ticket cost = "))
local_transp=int(input("Total transportation expenses= "))
total_food=travelling_days*daily_food
total_hotel=Hotel_charge*travelling_days
Total=total_food+total_hotel+ticket_cost+local_transp
company=Total+Total*10/100
avg=company/travelling_days
print(f'''
Nmae of employee = {name}

''')