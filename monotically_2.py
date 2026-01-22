from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == 1: return nums
        dq = deque()
        for end in nums[:k]:
            while dq and end > dq[-1]:
                dq.pop()
            dq.append(end)
        result = [dq[0]]
        for i in range (k, len(nums)):
            if dq[0] == nums[i - k]:
                dq.popleft()
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
            result.append(nums[i])
        return result
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
phongteo = Solution()
print (phongteo.maxSlidingWindow(nums, k))