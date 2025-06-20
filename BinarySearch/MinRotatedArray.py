## O(logn) time O(1) space

class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        return nums[left]
    

    ## Traditional binary search
    ## Check if mid value is greater than right value
        ## if it is move left over 
        ## if not move right to m
    ## return value where left and right are the same