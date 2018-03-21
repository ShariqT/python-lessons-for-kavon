#Kavon, this program is wrong. My name can't be both
#equal to 12 and more than 12 at the same time. Fix this
#so that it actually makes sense and only prints one of those lines
name = "Shariq Torres"
if len(name) == 13:
    print("My name takes up 12 spaces")
if len(name) > int("12"):
    print("My name takes up more than 12 spaces")
else:
    print("My name takes up less than 12 spaces")