class Solution(object):
    def reverseString(self, s):
        s.reverse()

## O(n) time O(1) space

class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1

## Make sure you swap left and right at the same time so you dont lose the original values of either

