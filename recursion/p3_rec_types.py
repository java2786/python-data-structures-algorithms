def demo1():
    print("Welcome")
    demo1() # rec call at tail

def demo2():
    demo2() # rec call at head
    print("Welcome")

def demo3(n):
    demo3(n-1) # rec call at tree
    demo3(n-2) # rec call at tree
    demo3(n-3) # rec call at tree
    print("Welcome")


# demo1()
# demo2()
demo3(5)