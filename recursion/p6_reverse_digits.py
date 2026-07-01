def reverse(num, res):

    # base case
    if(num==0):
        # print(res)
        return res

    # logic 
    ld = num%10
    res = (res * 10) + ld
    num = num // 10

    # recursion
    return reverse(num, res)

r = reverse(6785, 0)
print(r)