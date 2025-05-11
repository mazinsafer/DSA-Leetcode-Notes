## O(n^2) time, O(n) space

class Solution(object):
    def threeSome(self, nums):
        output = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while right > left: 
                if nums[i] + nums[left] + nums[right] == 0:
                    output.append([nums[left], nums[right], nums[i]])
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                    right = right - 1
                    while right > 0 and nums[right] == nums[right + 1]:
                        right = right - 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return output
     

## sort array to make it easier
## to check for triplets, left pointer is going to be right after the current num and right is going to be at the end
## add the current num, left, and right and see if they equal 0
        #if they equal 0, append the triplet and move the left and right pointers
        ## if the sum is less than 0, move the left pointer to the right
        ## if the sum is more than 0, move the right pointer to the left
## to check for duplicates for the current num, skip to the next num if the current num is equal to the one before
## to check for duplicates for left and right, keep moving left to the right and right to the left if they are equal to the before/after it