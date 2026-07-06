def reverse_string(name, rev):
    if(len(name)==0):
        print("Rev",rev)
        return

    print(f"First: {name[0]}, Remaining: {name[1:]}")
    # logic
    rev = name[0]+rev

    reverse_string(name[1:], rev)
name = "aman"

reverse_string(name, "")