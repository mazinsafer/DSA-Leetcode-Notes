class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        num_0 = 0
        max_w = 0
        while right < len(nums):
            if nums[right] == 0:
                num_0 = num_0 + 1
            right = right + 1

            while num_0 > k:
                if nums[left] == 0:
                    num_0 = num_0 - 1
                left = left + 1
            max_w = max(max_w, right - left)

        return max_w
    

## manipulating the length of the window
## left and right pointers, right will be moving over so it has to less than length of nums
## check if right is 0, if it is update num_zeros by 1 then move right over 
## once num_zeros is bigger than k, we cant move right any more. you must keep moving left over until num_zeros is less than  or equal to k
## check if left is 0, if it is decrement num_zeros by 1
## once num_zeros <= k, we have a valid window and can calculate the length of max_window and continue moving right over
