def isPalindrome(str, start, end):
    # base case
    if(start >= end):
        return True
    
    print(f"{start} -> {str[start]}, {end} -> {str[end]}")
    if(str[start]==str[end]):
        return isPalindrome(str, start+1, end-1)
    else:
        return False


name = "madam"
print(f"{name} -> {isPalindrome(name, 0, len(name)-1)}")

name = "anna"
print(f"{name} -> {isPalindrome(name, 0, len(name)-1)}")

name = "party"
print(f"{name} -> {isPalindrome(name, 0, len(name)-1)}")

name = "racecar"
print(f"{name} -> {isPalindrome(name, 0, len(name)-1)}")


