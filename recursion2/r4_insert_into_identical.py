def insertIntoIdenticalChars(str, index, res):
    # base case
    if(index == len(str)):
        res = res + str[-1]
        print(res)
        return

    # logic
    if(str[index] == str[index - 1]):
        res = res + str[index-1] + "*"
    else:
        res = res + str[index-1]
    # recursion call
    insertIntoIdenticalChars(str, index+1, res)    
    

insertIntoIdenticalChars("Leetcode", 1, "")