def find_sum(list, sum):
    for i in range(0, len(list)-1):
        for ni in range(i+1, len(list)):
            if(list[i]+list[ni]==sum):
                print(f"{list[i]} and {list[ni]}")
            
list = [1,2,3,4,2,0,5,-1]    
find_sum(list, 4)
