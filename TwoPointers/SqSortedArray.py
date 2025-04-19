## O(n) time and space
class Solution(object):
    def sortedSquares(self, nums):
        nums_sq = []
        output = []
        for num in nums:
            nums_sq.append(num ** 2)
        left = 0
        right = len(nums_sq) - 1 
        while right >= left:
            if nums_sq[right] > nums_sq[left]:
                output.append(nums_sq[right])
                right = right - 1
            else:
                output.append(nums_sq[left])
                left = left + 1
        output.reverse()
        return output
    

## array for the numbers squared
## array for output
## iterate through nums and append num^2 to nums_sq array
## left and right pointers for nums_sq
## while right >= left because
## if right value is bigger than left value append the right value to output, if left value is bigger than right value append left value to output
## move the right and left pointers to the left and right
## reverse output to sort it in increasing order
