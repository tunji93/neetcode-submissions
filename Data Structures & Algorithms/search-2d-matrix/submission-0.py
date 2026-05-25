class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        firstRow = 0
        lastRow = len(matrix) - 1



        def getRow(left, right):

            while left <= right:

                mid = (left + right) // 2

                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                
                if target < matrix[mid][0]:
                    right = mid-1
                else:
                    left = mid+1
            
            return -1
        
        row = getRow(firstRow, lastRow)
        if row == -1:
            return False
        
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid+1
            else:
                right = mid - 1
        return False

        