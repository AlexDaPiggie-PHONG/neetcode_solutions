def twoSum (nums: list[int], target: int) -> list[list[int]]:
    numdict = {}
    result = set()
    for num in nums:
        if num in numdict:
            subresult = sorted([-target, num, target - num])
            subresult = tuple(subresult)
            if subresult in result:
                continue
            else:
                result.add(subresult)
        else:
            numdict[target - num] = num
    return result

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        for i in range (len((nums))):
            target = -nums[i]
            subresult = twoSum(nums[:i] + nums[i + 1:], target)
            for element in subresult:
                if element in result:
                    continue
                else:
                    result.add(element)

        return list(result)

heomap = Solution()
nums = [-1,0,1,2,-1,-4]
print (heomap.threeSum(nums))