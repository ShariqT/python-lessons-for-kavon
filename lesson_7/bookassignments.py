#complete favorite_food = input("what is your favorite food?")
#complete print(favorite_food)
#complete favorite_food2 = input("what is your second favorite food? ")
#complete print(favorite_food2) 
#complete print(favorite_food + favorite_food2)

total_bill = input("what's the total bill? ")
x = float(total_bill)
tip_fifteen = x*.15
tip_fifteen = int(tip_fifteen)
tip_twenty = x*.20
tip_twenty = int(tip_twenty)
print("A 15% tip is", int(tip_fifteen), "dollars.")
print("A 20% tip is", int(tip_twenty), "dollars.")
print("Your total bill plus a 15% tip is", float(total_bill)+int(tip_fifteen), "dollars.")
print("Your total bill plus a 20% tip is", float(total_bill)+int(tip_twenty), "dollars")