## Not as Optimal, Average O(n) time O(1) space, but O(n^2) time in the worst case due to the del if all elements in nums are duplicates
def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                del nums[i]
            else:
                i = i + 1
        return len(nums)

## Most Optimal solution, Always O(n) time O(1) space
def removeDuplicates(self, nums):
        j = 0 ## j is the number of unique elements
        for i in range(1,len(nums)): ## skip the first number in nums
            if nums[j] != nums[i]: ## if the first number in nums does not equal the second number 
                j = j + 1 ## then increment j because we found a unique number
                nums[j] = nums[i] ## and also skip index j to i to keep going
        return j + 1 ## return the len of nums with j elements