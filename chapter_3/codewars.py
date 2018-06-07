def DNA_strand(dna):
    return_value = ""
    for i in dna:
        print(i)
        
        if i == "A":
            return_value +="T"
        if i == "T":
            return_value +="A"
        if i == "C":
            return_value +="G"
        if i == "G":
            return_value += "C"
    print(return_value)
    return return_value
DNA_strand("AAA")
        