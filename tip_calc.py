bill = float(input("enter total bill amount:"))
tip_percent = float(input("enter tip percentage:"))

tip = bill * (tip_percent/100)
total = bill + tip

print("tip amount:",tip)
print("total amount to pay:",total)
