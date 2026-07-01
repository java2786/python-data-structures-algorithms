def power(n, p, r=1):
    print(f"N: {n}, P: {p}, R: {r}")
    # base case
    if(p==0):
        return r 

    # logic
    r = r * n 
    p = p-1


    # recursion call
    return power(n, p, r)


result = power(3, 3) # 27
print(result)