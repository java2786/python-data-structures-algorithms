def find_rev(ld,rev,n):
    if(ld == 0):
        print(rev)
        return
    ld = n % 10 
    rev = rev * 10 + ld
    n = n // 10
    
    find_rev(ld,rev,n)

find_rev(3456,0,3456)