## O(n) time and space

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)  ## initiliaze answer array to all ones and same len as nums
        prefix = 1 ## prefix product
        suffix = 1 ## suffix product
        for i in range(len(nums)): ## prefix pass (left to right)
            answer[i] = prefix 
            prefix = prefix * nums[i]
        ## now, answer will have the product of everything to the left of the number

        for i in range(len(nums)-1, -1, -1): ## suffix pass (right to left)
            answer[i] = answer[i] * suffix 
            suffix = suffix * nums[i]
        ## now going from right to left, we just multiply the current answer[i] by the product of the numbers after it which is suffix

        return answer  ## were returning answer which is the product of the prefix values and suffix values


## whats happening is we need 2 loops: 1 for the prefix vals, and then a second for the final vals

## You first initialize answer[i] to the product of everything to the left of nums[i]. For index i = 0, this is 1 (nothing is to the left).
##You then update prefix to include nums[i] by multiplying it by nums[i], so that future indices will have the product of all elements before them.

## You then process the array from right to left, multiplying answer[i] by the product of all elements to the right of nums[i], which is stored in suffix.
## As you iterate, you update suffix by multiplying it with nums[i].
