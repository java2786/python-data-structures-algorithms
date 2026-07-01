def countDigits(num=0, c=0):
    if(num==0):
        print(c)
        return
    num = num // 10
    c = c+1

    countDigits(num, c)


countDigits(321)