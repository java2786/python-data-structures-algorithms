# remove consecutive chars
def remove_consecutive(str, index, res):
    # base case
    if(index==len(str)):
        print(res)
        return

    if(index==(len(str)-1)):
        res += str[index]
        index = index+1
    # logic
    elif(str[index] == str[index+1]):
        index = index + 1 + 1
    else:
        # res = res + str[index]
        res += str[index]
        index = index+1

    # recursion call
    remove_consecutive(str,  index, res)

# H E L L O
# 0 1 2 3 4

# D E M M O O S
# 0 1 2 3 4 5 6

remove_consecutive("demmoos",  0, "")