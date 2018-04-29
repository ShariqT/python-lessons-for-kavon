from password_manager.database import passwords
from password_manager.input import enter_passwords
import os
def add_entry():
    os.system("clear")
    keep_going = True
    database_entry = enter_passwords()
    while keep_going == True:
        answer = input("Would you like to add another entry? Enter yes or no " )

        if answer == "yes" :
            call = enter_passwords()
            print(call)
        else:
            keep_going = False
            main_menu()

def print_entry():
    os.system("clear")
    print(passwords)
    main_menu()

def main_menu():

    print("what would you like to do?" )
    print("1)add entry")
    print("2)print entry")
    print("3)quit")
    user_choice = input("enter choice: ")
    
    if user_choice == str(1):
        add_entry()
    if user_choice == str(2):
        print_entry()
    if user_choice == str(3):
        print("I guess I'll see you next lifetime...")
main_menu()