class Solution(object):
    def twoSum2(self, nums, target):
        dic = {} # 2:0, 7:1, 9:2, 
        for i in range(len(nums)):
            diff = target - nums[i] # 11
            if diff in dic:
                # print(f"prev: {diff}, curr: {nums[i]}")
                # return [diff, nums[i]]
                return [dic[diff], i]
            else:
                dic[nums[i]] = i

sol = Solution()
nums = [1,2,3,4,5]
target = 3
print(sol.twoSum2(nums, target))
