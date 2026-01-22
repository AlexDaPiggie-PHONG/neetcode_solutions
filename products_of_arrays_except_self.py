'''
Docstring for products_of_arrays_except_self
nums = [1,2,4,6], len = 4
left = [1, 1, 2, 8]
nums = [6,4,2,1]
right = [1,6,24,48]
right = [48, 24, 6, 1]
- 1=> -len + 1
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [None]*len(nums)
        left = [1]
        right = [1] * len(nums)
        print ("DEBUG: right index in the beginning", right) 

        for i in range (1, len(nums)): #i: 1 -> 3
            num = nums[i - 1] * left[i - 1]
            left.append(num)

        for i in range (1, len(nums)):
            num = nums[-i] * right[-i]
            right[-i - 1] = num
        
        for i in range(len(left)):
            result[i] = left[i] * right[i]
        
        return result
    
solulu = Solution()
nums = [1,2,4,6]
print (solulu.productExceptSelf(nums))
        