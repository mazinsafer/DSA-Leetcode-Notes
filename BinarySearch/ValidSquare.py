## O(logn) time O(1) space

class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num
        while left < right:
            m = (left + right ) // 2
            prod = m ** 2
            if prod > num:
                right = m
            elif prod < num:
                left = m + 1
            else:
                return True
        if left and right == 1:
            return True
        return False
    
    # Perform conditional binary search from 1 to n
    ## checking if the current middle squared is greater than or equal to num
    ## from there you can adjust left and right pointers based on how big m ^ 2 is