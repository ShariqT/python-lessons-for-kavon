Word1 = input("what word would you like to use?")
Word2 = input("what word would you like to use?")
Word3 = input("what word would you like to use?")
print(Word1[0]+Word2[0]+Word3[0])

firstlettersof3words = Word1[0]+Word2[0]+Word3[0]
if firstlettersof3words == "cat":
    print("meow")
else:
    print(firstlettersof3words)
