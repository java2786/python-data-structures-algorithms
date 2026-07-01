def isPalindrome(num, rev, original):
    if(num==0):
        if(rev == original):
            print(f"Num: {original}, Reverse: {rev}, Palindrome")
        else:
            print(f"Num: {original}, Reverse: {rev}, Not Palindrome")
        return
    # ld = num%10
    # rev = rev*10 + ld
    # isPalindrome(num//10, rev)

    isPalindrome(num//10, (rev*10)+(num%10), original)

mynum = 1212
isPalindrome(mynum, 0, mynum)