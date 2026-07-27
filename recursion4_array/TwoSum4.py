class Solution(object):
    def twoSum4(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]

sol = Solution()
nums = [7,6,5,2,8]
target = 12
print(sol.twoSum4(nums, target))
