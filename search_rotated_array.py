def binarySearch (nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len (nums) == 1:
            if nums[0] == target: return 0
            else: return -1
        
        #find cut position
        cut = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                cut = left
                break 
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else: 
                right = mid
            
        s1 = []
        if cut > 0:
            s1 = nums[:cut]
        s2 = nums[cut:]
        if s2[-1] >= target:
            res = binarySearch(s2, target)
            if res != -1:
                return cut + res
            else:
                return -1 
        elif s2[-1] < target and s1:
            res = binarySearch(s1, target)
            return res
        else:
            return -1

nums = [3,4,5,6,1,2]
target = 1
phongteo = Solution()
print (phongteo.search(nums, target))
