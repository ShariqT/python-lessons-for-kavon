from password_manager.database import create_db_entry
from password_manager.input import enter_info
import os

def add_entry(passwords):
    os.system("clear")
    keep_going = True
    database_entry = enter_info()
    
    passwords = create_db_entry(passwords, database_entry)
    while keep_going == True:
        answer = input("Would you like to add another entry? Enter yes or no " )

        if answer == "yes" :
            new_record = enter_info()
            passwords = create_db_entry(passwords, new_record)
            
            print(new_record)
        else:
            keep_going = False
    
    return passwords

def print_entry(paaswords):
        for i in passwords:
            print(i)
        os.system("clear")
        print(passwords)
        main_menu(passwords)


def main_menu(passwords):

    print("what would you like to do?" )
    print("1)add entry")
    print("2)print entry")
    print("3)quit")
    user_choice = input("enter choice: ")
    
    if user_choice == str(1):
        passwords = add_entry(passwords)
        main_menu(passwords)
    if user_choice == str(2):
        print_entry(passwords)
    if user_choice == str(3):
        print("I guess I'll see you next lifetime...")

passwords = []
main_menu(passwords)