'''
Docstring for two_sum
4, 5 ,6
i = 0
    nums[i] not in doodoo
        doodoo[0] = target - 4 = 10 - 4 = 6
        doodoo = 0
i = 1
    nums[i] not in doodoo
    doodoo[i] = target - 5 = 5
    doodoo = 0,5
 
i = 2
    nums[i] in doodoo
    j in range doodoo
        j = 0: doodoo[i] = nums[i] = 6
        return j, i: {0,2}
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        doodoo = {}
        for i in range (len(nums)):
            if nums[i] not in doodoo.values():
                doodoo[i] = target - nums[i]
            else:
                for j in range (len(doodoo)):
                    if doodoo[j] == nums[i]:
                        return [j,i]
                    

solulu = Solution ()
nums = [4,5,6]
target = 10
print (solulu.twoSum(nums, target))
