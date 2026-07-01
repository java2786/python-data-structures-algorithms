nums = [1,2,3,4,5]

i = 0
j = len(nums)-1
while(i<j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
	i= i+1
	j= j-1
	
print(nums)