def print_name(fname,lname, count):
    if(count==0):
        return
    print(f"{count}: {fname}")
    print_name(fname, lname, count-1)
    print(f"{count}: {lname}")

print_name("mohit","chaudhary", 5)


