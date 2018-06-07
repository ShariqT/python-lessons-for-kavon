# Kavon, I want you to make a program that will let me enter a username
# and a password. After that I want the program to print out both the username
# and the password I just entered.

# With the password I just entered, I want to you to check to see if this
# is equal to the root_password variable. If it is, then print "Access Granted"; if it is not, 
# then print "Access Denied"

# Kavon, I just realized that I need to make sure my password is really
# hard to guess. Make it so that the program checks to make sure the 
# entered password is strong! First we need to make sure that the password is 
# more than 8 characters long. The second thing we need to make the password
# strong is make sure it begins with an exclaimation point. If the password is
# strong then print a message that says, "strong password". if not, then 
# print "weak password"

root_password = "boogeyman123"
name = "kavon"
password = input("What is your password?")
print("your user name is:"+ (name))
print("your password is:", password)

if root_password == password :
    print("stop being a copy cat")
if root_password != password :
    print("access granted, you are creative")
if password[0] == "F" or password[0] == "U" and len(password)==8:
    print("Strong password!")
else:
    print ("weak password")

    
    