
def greet(name, count):
    input()
    if(count==6):
        return
    print(f"{count}. Welcome {name}")
    greet(name, count+1)
    input()
    print(f"{count}. Welcome {name}")

greet("Ramesh", 1)
print("ByeBye")