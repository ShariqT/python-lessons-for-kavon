# Kavon, we have a list of tuples here that has the user information
# I wrote some of this program, but its not working. It is supposed to 
# print out your favorite team when you enter your name. Fix this program so
# that I can enter any of the three usernames and the correct favorite team 
# is printed. 
# Note: you cannnot add new code to this program, but you can alter the existing code

users = [
    ('shariq', 'testP@ss', 'Cavs'),
    ('kavon', 'passW0rd', 'Knicks'),
    ('jason', 'p@ssword', 'Lakers')
]

username = input("Enter your username: ")
for user in users:
    if user[2] == username:
        selected_user = user
print(selected_user[0] + " favorite team is " + selected_user[1])