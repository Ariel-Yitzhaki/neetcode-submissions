class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if matrix[0][0] > target  or matrix[rows - 1][cols - 1] < target:
            return False

        l, r = 0, rows

        while l < r - 1:
            m = l + ((r - l) // 2)
            if matrix[m][0] > target:
                r = m - 1 # Because we check for [0][0] we don't need to worry about m being 0 when > target
            elif matrix[m][0] < target:
                l = m
            elif matrix[m][0] == target:
                return True

        ind = r if r == l else l
        l = 0
        r = cols
        while l < r:
            m = l + ((r - l) // 2)
            if matrix[ind][m] > target:
                r = m
            elif matrix[ind][m] < target:
                l = m + 1
            elif matrix[ind][m] == target:
                return True

        return True if l < cols and matrix[ind][l] == target else False

        