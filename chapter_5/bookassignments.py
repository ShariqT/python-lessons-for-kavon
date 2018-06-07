points_pool = 30
attributes = {"Health":0, "Strength":0, "Wisdom":0, "Dexterity":0}
print("Type 1 for Health, 2 for Strength, 3 for Wisdom and 4 for Dexterity")
choice = input("What would you like to spend your money on?")
if choice == "1":
    print("You have chosen the Health attribute, and it's current value is" + str(attribute["Health"]))
elif choice == "2":
    print("You have chosen the Strenght attribute, and it's current value is" + str(attribute["Strength"]))
elif choice == "3":    
    print("You have chosen the Wisdom attribute, and it's current value is" + str(attribute["Wisdom"]))
elif choice == "4":   
    print("You have chosen the Dexterity attribute, and it's current value is" + str(attribute["Dexterity"])) 
else:
    print("Sorry, you fucked up, that is not an option")   