class Solution(object):
    def findMaxAverage(self, nums, k):
        total = 0
        for i in range(k):
            total = total + nums[i]
        max_average = float(total) / k

        for i in range(k, len(nums)):
            total = total - (nums[i-k])
            total = total + nums[i]
            average = float(total) / k
            if average > max_average:
                max_average = average

        return max_average
    

## Fixed sliding window of length k
## In the initial loop, find the average of the first k numbers

## In the second loop, iterate through the rest of nums
## to slide the window to the right, adding the next number to the running sum and subtract by the number you left out when you slid
## check if the avg of these numbers is bigger than max_average
## return max_average