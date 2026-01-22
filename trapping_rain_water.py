class Solution:
    def trap(self, height: list[int]) -> int:
        size = len(height)
        area = 0
        maxLeft = height[0]
        maxRight = height[size - 1]
        left = [maxLeft] * size
        right = [maxRight] * size
        for i in range (1, size):
            left[i] = maxLeft
            if height[i] > maxLeft: maxLeft = height[i]

            right[size - 1 - i] = maxRight
            if height[size -1 - i] > maxRight: maxRight = height[size - i - 1]

        for i in range (size):
            subarea = min(left[i], right[i]) - height[i]
            if subarea <= 0:
                continue
            else:
                area += min(left[i], right[i]) - height[i]
                
        return area
    
hellobantre = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print (hellobantre.trap(height))
        