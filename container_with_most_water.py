class Solution:
    def maxArea(self, heights: list[int]) -> int:
        size = len(heights)
        start = 0
        end = size - 1
        result = 0
        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            result = max(area, result)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -=1
        return result

toilaconheo = Solution()
height = [1,7,2,5,4,7,3,6]
print (toilaconheo.maxArea(height))