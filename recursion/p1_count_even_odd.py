def countEvenOdd(num, ecount, ocount):
    # base case
    if(num==0):
        print("even:",ecount)
        print("odd:",ocount)
        return

    # small problem
    if(num%2==0):
        ecount = ecount + 1
    else:
        ocount = ocount + 1

    # rec call
    countEvenOdd(num-1, ecount, ocount)

countEvenOdd(10, 0, 0)