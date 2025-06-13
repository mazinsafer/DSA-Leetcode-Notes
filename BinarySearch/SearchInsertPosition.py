## O(logn) time O(1) space
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        if target < nums[m]:
            return m
        return m + 1
    

    ## Perform regular binary search 
    ## For cases where the target is not already in the array nums,
        ## Eventually left, right, and m will be at the same value
        ## So if target is less than those values return m
        ## if not return m + 1
        