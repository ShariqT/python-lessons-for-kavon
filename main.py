from password_manager.database import passwords
from password_manager.input import enter_passwords

keep_going = True

while keep_going == True:
    answer = input("Would you like to add an entry? " )

    if answer == "yes" :
        call = enter_passwords()
        print(call)
    else:
        keep_going = False
        print("I QUIT!")
     
