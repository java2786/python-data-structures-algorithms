"""

=> string, find_char, replace_with, result

Find first char if same as given char
    yes -> res + change
    no -> res + first_char

remove first char and pass to recursion

"""

def search_replace(str, find_char, replace_with, result):
    # base case
    if(len(str)==0):
        print(result)
        return
    # logic
    if(str[0]==find_char):
        result = result + replace_with
    else:
        result = result + str[0]
    # recursion call
    search_replace(str[1:], find_char, replace_with, result)

search_replace("Hello", "l", "m", "")
