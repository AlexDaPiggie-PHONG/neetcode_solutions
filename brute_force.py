class Solution:
    def maxSlidingWindow (self, nums: list[int], k : int) -> list[int]:
        if k == 1: return nums
        result = []
        for start in range (len(nums) - k + 1):
            max_num = nums[start]
            for end in range (start + 1, start + k):
                max_num = max(max_num, nums[end])
            result.append(max_num)
        return result

nums = [1,2,1,0,4,2,6]
k = 3
alex = Solution()
print (alex.maxSlidingWindow(nums, k))