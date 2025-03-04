class Solution(object):
    def findClosest(self, nums):
        curr = nums[0] ## set curr = to the first number in the array
        for i in range(1, len(nums)): ## iterate starting at index 1, length of nums
            if abs(nums[i]) < abs(curr): ## if the absval of nums[i] is less than the abs val of curr
                curr = nums[i] ## then set curr = to the lesser number 
            if abs(nums[i]) == abs(curr) and nums[i] > curr: ## if their absval are equal but curr is negative
                curr = nums[i] ## then set curr = nums [i]
        return curr ## return curr
    

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
        # Time: O(n)
        # Space: O(1)