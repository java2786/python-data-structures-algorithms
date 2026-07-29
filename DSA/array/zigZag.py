from typing import List

class Solution:
    def zigZag(self, arr: List[int]) -> None:
        for i in range(len(arr)-1):
            # i is even
            if(i%2==0):
                if arr[i] > arr[i + 1]:
                    # swap
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
            # i is odd 
                if arr[i] < arr[i + 1]:
                    # swap
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
sol = Solution()
# arr = [4, 3, 7, 8, 6, 2, 1]
arr = [4, 7, 3, 8, 2]
sol.zigZag(arr)

print(arr)