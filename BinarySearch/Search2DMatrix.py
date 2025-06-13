## O(nlogn) time O(1) space

class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            left = 0
            right = len(row) -1
            while left <= right:
                m = (left + right) // 2
                if target == row[m]:
                    return True
                elif target > row[m]:
                    left = m + 1
                else:
                    right = m - 1
        return False


        ## For each row in the matrix perform binary search for the target number