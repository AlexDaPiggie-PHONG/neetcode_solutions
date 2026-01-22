'''
Docstring for longest_consecutive_sequence
o(n)
Input: nums = [2,20,4,10,3,4,5]
set num_set = nums
length = 0
checked = {}
for num in num_set
    if num not in checked:
        chekced[num] = 1
    else:
        con=t
    target = num + 1
    tempLength = 0
    while target in num_set
        tempLength += 1
        length = max(length, tempLength) 
        target = num + 1
        
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        num_set = set(nums)
        length = 1
        checked = {}
        for num in num_set:
            tempLength = 0
            if num not in checked:
                checked[num] = 1
            else:
                continue
            
            target = num + 1
            tempLength = 1
            while target in num_set:
                tempLength += 1
                length = max(length, tempLength)
                target += 1
        return length


phongteo = Solution()
nums = [2,20,4,10,3,4,5]
print (phongteo.longestConsecutive(nums))