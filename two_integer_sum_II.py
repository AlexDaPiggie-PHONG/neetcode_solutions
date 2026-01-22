'''
Docstring for two_integer_sum_II
numbers = [1,2,3,4]
doodoo[i] = target - nums[i]
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        size = len(numbers)
        doodoo = {}
        for i in range (size):
            if numbers[i] not in doodoo:
                doodoo[target-numbers[i]] = i
            else:
                return [doodoo[numbers[i]] + 1, i + 1]
        return []

phongteo = Solution()
numbers = [1,2,3,4]
target = 3
print (phongteo.twoSum(numbers, target))