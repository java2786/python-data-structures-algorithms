
def greet(name, count):
    if(count==6):
        return
    # name = f"Mr. {name}"
    greet(name, count+1)
    print(f"{count}. Welcome {name}")

greet("Ramesh", 1)
print("ByeBye")