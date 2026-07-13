def printStars(n):
    if(n==0):
        print()
        return
    print("* ", end="")
    printStars(n-1)


def printRow(r):
    if(r==0):
        return
    printRow(r-1)
    printStars(r)


# printStars(1)
# printStars(2)
# printStars(3)
# printStars(4)
# printStars(5)

printRow(5)