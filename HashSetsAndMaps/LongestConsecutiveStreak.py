## O(n) time and space

class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        j = 1
        streak_length = 0
        for num in s:
            if num - 1 in s:
                continue
            else:
                while num + j in s:
                    j = j + 1
                if num + j not in s:
                    if j > streak_length:
                        streak_length = j
                    j = 1
                    continue
        return streak_length

## Use a hashset for O(1) lookups to check if num is in the set
## Use j as a counter to add to num if num + j is in the set to check for a consequtive sequence
## Initalize j to 1
## streak_length is the biggest streak we were able to have
## iterate through the numbers in the set
## if the num - 1 is in the set, skip it because it cant be the start of a sequence
## Once you find a num that could be the start of the sequence:
            ## keep adding j to it until num + j isnt in the set anymore using a while loop
            ## if j > streak length then j is the new biggest streak length
            ## eventually num + j wont be in the set, so reset j back to 1 and go the next num
## after going through all the nums, return streak_length which is the biggest consecutive streak

