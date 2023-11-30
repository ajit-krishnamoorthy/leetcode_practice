class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows*columns - 1
        while left <= right:
            mid = (left+right)//2
            element = matrix[mid // columns][mid % columns]
            if target == element:
                return True
            elif target > element:
                left = mid + 1
            elif target < element:
                right = mid - 1
        return False