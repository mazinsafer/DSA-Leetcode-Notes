## O(n) time O(1) space

class Solution(object):
    ## use max to save your self time
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        currArea = 0
        maxArea = 0
        while right > left:
            currArea = (right - left) * min(height[left], height[right])
            if currArea >= maxArea:
                maxArea = currArea
            if height[left] <= height[right]:
                left = left + 1
            elif height[right] < height[left]:
                right = right - 1

        return maxArea
    
# left pointer at beginning of array, right pointer at the end
## currArea will be the current Area of the values of the current left and right pointers
## maxArea is the current maximum Area, which is what we want to return. we will be updating this if the currArea is >
## while right>left, calculate the currArea which is length * width
        ## length is the difference in indexes between the two numbers
        ## width will be the shorter number 
## if currArea is bigger than maxArea, currArea is the new maxArea
## if value on the left is > than the value on the right, move right to the left
## if value on the right is > than the value on the left, move left to the right
## if the values are equal nothing happens, so to progress move either the left or right pointers, either will work