## O(logn) time O(1) space
class Solution(object):
    def search(self, nums, target):
        left = 0 
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            
            if nums[left] <= nums[m]:
                if nums[left] <= target <= nums[m]:
                    right = m - 1
                else:
                    left = m + 1

            else:
                if nums[m] <= target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1

        return -1
    

## check if the left half is sorted
    ## if it is check if target is in the left half

## if not go to the right half and check if target is in the right half

## return m when target == nums[m]
