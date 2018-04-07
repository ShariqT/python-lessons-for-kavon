# Kavon, this program is messed up somewhere
# What am I doing wrong? When I put in Tic1kli2h as
# my password and 8 as my magic number, I don't have access
# Either tell me the correct password and magic number combination
# or change the program so that my password/magic number works.

password = ["T","i","c",1,"k","l","i",2,"h"]

challenge = input("Enter your password: ")
if challenge[2] == password[2]:
    secret_number = input("Enter your magic number: ")
    if secret_number == str(8):
        print("Access Granted!")
else:
    print("Access Denied")