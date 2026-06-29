def getSum(num, sum):
    if(num==0):
        return sum
    
    return getSum(num//10, (num%10)+sum)

sum = getSum(565434587, 0) 

print(sum)
# output => 10