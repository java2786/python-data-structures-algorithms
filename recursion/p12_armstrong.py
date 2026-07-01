def countDigits(num=0, c=0):
    if(num==0):
        return c
    num = num // 10
    c = c+1

    return countDigits(num, c)

def power(n, p, r=1):
    # base case
    if(p==0):
        return r 

    # logic
    r = r * n 
    p = p-1


    # recursion call
    return power(n, p, r)

def getSum(num, sum=0):
    if(num==0):
        return sum

    ld = num%10
    num = num//10

    return getSum(num, sum+ld)


def isArmstrong(num, c, originalNum, sum):
    print(f"Num: {num}, C: {c}, Original: {originalNum}, Sum: {sum}")
    # input()
    # base case
    if(num==0):
        return sum == originalNum 
    # logic
    
    # 2. power
    p = power(num%10, c)
    # 3. sum
    sum = sum + p 

    # recursion call
    return isArmstrong(num//10, c, originalNum, sum)

num = 765
sum = 0
c = countDigits(num)
flag = isArmstrong(num, c, num, sum)

print(flag)