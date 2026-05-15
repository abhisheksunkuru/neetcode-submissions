class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, h = 0, (m*n)-1
        while l<=h:
            mid = (l+h)//2
            mid_val = matrix[mid//n][mid%n]
            if mid_val == target:
                return True
            elif mid_val > target:
                h = mid - 1
            else:
                l = mid + 1

        return False            


            