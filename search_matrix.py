class Solution:
    def searchMatrix (self, matrix : list[list[int]], target : int) -> bool:
        if not matrix: return False
        if len(matrix) == 1 and len(matrix[0]) == 1: 
            return matrix[0][0] == target
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        left, right = 0, row * (col + 1) + col
        while left <= right: 
            box = left + (right - left) // 2
            i = box // (col + 1)
            j = box % (col + 1)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = box + 1
            else:
                right = box - 1
        return False
    
phongteo = Solution()
matrix = [[1,3]]
target = 3

# matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target=15
print (phongteo.searchMatrix(matrix, target))