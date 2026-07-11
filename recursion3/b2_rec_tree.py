def branch(n):
    if(n<=0):
        print("Base Case:",n)
        return
    print(n,"Calling (n-1):",(n-1))
    branch(n-1)
    print(n,"Calling (n-2):",(n-2))
    branch(n-2)
    print(n,"Calling (n-3):",(n-3))
    branch(n-3)


branch(2)
branch(3)
branch(5)