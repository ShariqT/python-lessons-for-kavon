import random

names = ['cat', 'bat', 'hat']
already_printed = []

while len(names) != len(already_printed):
    random_number = random.randint(0,2)
    if random_number not in already_printed:
        print(names[random_number])
        already_printed.append(random_number)
    
    else:
        continue
    