# Kavon, I want to make a scanning program that will let me 
# know if there are any special characters in a user's password. 
# Special characters -- for this program only -- can be defined 
# as the following: ! @ # $ % ^ & *
# If you find any of the following, then the program should
# stop the loop and print out a message saying "I found a special character!"
# Hint: you'll need to use the len() function/command to find the length of
# the user's password so you will know how long to loop
# Hint: You can only add to this program; you can't mess with the user_password
# and counter variable

user_password = input("What is your password? ")
counter = 0
  
while counter <= len(user_password):
    user_password[counter]
    if user_password[counter] == "!":
        print("I found a special character!")
        break
    if user_password[counter] == "@":
        print("I found a special character!")
        break
    if user_password[counter] == "#":
        print("I found a special character!")
        break
    if user_password[counter] == "$":
        print("I found a special character!")
        break
    if user_password[counter] == "%":
        print("I found a special character!")
        break
    if user_password[counter] == "^":
        print("I found a special character!")
        break
    if user_password[counter] == "&":
        print("I found a special character!")
        break
    if user_password[counter] == "*":
        print("I found a special character!")
        break
    counter+=1
