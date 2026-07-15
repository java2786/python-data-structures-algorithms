
def solution(list, element, index, res):
	if(index == len(list)):
		return res

	if(list[index]==element):
		res.append(index)

	return solution(list, element, index+1, res)

result = solution([4,3,5,2,5,6], 5, 0, [])

print(result)