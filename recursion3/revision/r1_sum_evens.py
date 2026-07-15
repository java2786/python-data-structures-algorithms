def sumEvens(list, index, sum):

	# base case
	if(index==len(list)):
		print(sum)
		return
	# logic
	if(list[index]%2==0):
		sum = sum + list[index]

	# recursion call
	print(index)
	sumEvens(list, index+1, sum)

list = [4,3,1,6]
sumEvens(list, 0, 0)