## Python based tip calculator:
#input bill
bill = float(input("enter total bill amount:"))

#input tip_percent:
tip_percent = float(input("enter tip percentage:"))

#formulising tip 
tip = bill * (tip_percent/100)

##total
total = bill + tip

#final step of printing tip amount and total amount to pay:
print("tip amount:",tip)
print("total amount to pay:",total)
