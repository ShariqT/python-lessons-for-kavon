# Kavon something is wrong with this program. It should only
# say 'Access Granted' to admin users. Also, it says 'Access Granted'
# or 'Access Denied' three times before stopping. It should only print
# this message out once.

# I also want to give users a maximum of three tries of putting 
#in their username/password. You can change anything want in this
# this program except for the 'users' variable.  


users = [
    ('shariq', 'testP@ss', 'Cavs', 'Admin'),
    ('kavon', 'passW0rd', 'Knicks', 'NoAdmin'),
    ('jason', 'p@ssword', 'Lakers', 'NoAdmin')
]


username = input("enter your username: ")
password = input("enter your password: ")

for user in users:
    if user[1] == password:
        print("Access Granted!")
        print("Welcome, " + user[0])
    else:
        print("Access Denied!")