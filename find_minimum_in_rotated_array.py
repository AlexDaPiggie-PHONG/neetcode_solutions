class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
            
        return -1

nums = [3,4,5,6,1,2]
alex = Solution()
print (alex.findMin(nums))