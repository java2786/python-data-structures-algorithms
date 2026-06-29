def getSum(num, sum):
    if(num==0):
        print(sum)
        return

    ld = num%10
    num = num//10

    getSum(num, sum+ld)

getSum(12347, 0) 

# output => 10