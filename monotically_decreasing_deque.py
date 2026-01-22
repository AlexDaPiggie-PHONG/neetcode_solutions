from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums: return []
        if k == 1: return nums
        start = end = 0
        dq = deque()
        result = []
        for end in range (len(nums)):
            while dq and nums[end] > nums[dq[-1]]:
                dq.pop()
            dq.append(end)
            if dq[0] < start: 
                dq.popleft()
            if end + 1 >= k: 
                result.append(nums[dq[0]])        
                start += 1
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
phongteo = Solution()
print (phongteo.maxSlidingWindow(nums, k))