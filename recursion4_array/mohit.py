def find_sum(list, sum, count, index, next_index):
    print(f"count: {count}, index: {index}, NI: {next_index}")
    # base case - index
    if(index==len(list)-1):
        print(f"Index reached to end: {index} - return")
        return
    # base case - ni
    if(next_index == len(list)):
        newIndex = index+1
        count = count + 1
        find_sum(list, sum, count, newIndex, newIndex+1)
        return

    # logic 
    if(list[index]+list[next_index]==sum):
        print(f"{list[index]} and {list[next_index]}")

    # recursion call / small problem
    find_sum(list, sum, count, index, next_index+1)

list = [1,2,3,4,2,0,5,-1]    
find_sum(list, 4, 0, 0, 1)
