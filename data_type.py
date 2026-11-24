# cost=eval(input("Enter cost price: "))
# mrp=eval(input("Enter mrp : "))
# profit=mrp-cost
# per=mrp*profit/100
# print(f'''
# Profit is= {profit}
# percantage= {per}
# ''')


# g_rate=eval(input("Enter the gold rate= "))
# amount=eval(input("Enter amount of gold(gram)= "))
# making=eval(input("Enter making charges= "))
# total=g_rate*amount
# make=total*making/100
# gst=total-total+make*3/100
# final=total+make+gst
# print(f'''
# total amount of gold(gram)= {amount}
# price of gold= {total}
# making charges= {make}
# gst= {gst}
# final bill to pay= {final}
# ''')

principal=eval(input("Enter principal amount= "))
annual_r=eval(input("Enter annual rate= "))
time=eval(input("Enter time(year)= "))
a=principal*(1+annual_r/100)**time
print(f'''
Principal amount is= {principal}
Annual rate= {annual_r}
Time (year)= {time}
Campound intrest is= {a}''')
