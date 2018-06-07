# The homework for this week is going to be going over 
# for loops again. Take the variable "my_name" and print
# every other letter. the resulting message should be
# "hello kavon" in all caps

# hint: you cannot change the my_name variable
# hint: you will need to use the len() function to find the length of my_name



#odd_numbers = "HELLO KAVON"
#print(odd_numbers)

my_name = "gHiEmLpLqOm lKwAeViObN"

print("22 = {}".format(len(my_name)))
final_val = ""
for i in range(1,len(my_name),2):
    final_val += my_name[i]
print(final_val)    