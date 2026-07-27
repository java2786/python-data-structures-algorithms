def twoSum(nums, target, index, result ):

    if(target==0 and len(result)==2):
        return result

    # out of range
    if(index == len(nums)):
        return None
    # length
    if (len(result)>2):
        return None

    # less than zero
    if(target<0):
        return None



    answer = twoSum(nums, target - nums[index], index+1, result+[nums[index]])

    # answer is none
    if(answer):
        return answer
    else:
        return twoSum(nums, target, index+1, result)

list = [7,3,6,5, 8]
target = 15
resultList = twoSum(list, target, 0, [])
print(resultList)