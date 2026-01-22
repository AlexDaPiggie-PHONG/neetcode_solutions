import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 0, max(piles)
        result = 0
        while left <= right:
            # print (f"DEBUG: left = {left} and right = {right}")
            k = left + (right - left) // 2
            # print (f"DEBUG: k = {k}")
            if k == 0: return result
            hour = 0
            for banana in piles:
                # hour += (banana // k) + 1
                hour += math.ceil (banana / k)
            # print (f"DEBUG: hour = {hour}")
            if hour <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result
    