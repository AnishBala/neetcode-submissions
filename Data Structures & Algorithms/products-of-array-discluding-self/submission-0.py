#array output

#for each element in array nums, multiply each element except the current element and add it to array "output"
    # for element in nums
        # temp var to store how far it is from the left
            #loop add to running product total
        # temp var to store how far it is from right
            #loop add to running product total

#return output

#32 bit integer 


#have left, nums
#can multiply left by corresponding nums element up until current
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        #left
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        #right
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            
        
        #have left and right array
        for i in range(n):
            output[i] = left[i] * right[i]

        return output


#edge cases: 




        