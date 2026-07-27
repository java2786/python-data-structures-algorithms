class Solution(object):
    def twoSum(self, nums, target):
        return self.myTwoSum(nums, target, 0, [] )

    def myTwoSum(self, nums, target, index, result ):
        if(target==0 and len(result)==2):
            return result
        if(index == len(nums)):
            return None
        if (len(result)>2):
            return None
        # if(target<0):
        #     return None

        answer = self.myTwoSum(nums, target - nums[index], index+1, result+[index])

        if(answer):
            return answer
        else:
            return self.myTwoSum(nums, target, index+1, result)


sol = Solution()
nums = [-1,-2,-3,-4,-5]
target = -8
print(sol.twoSum(nums, target))