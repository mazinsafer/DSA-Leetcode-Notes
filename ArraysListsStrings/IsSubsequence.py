## O(n) time O(1) space
class Solution(object):
    def isSubsequence(self, s, t):
        if not s: ## Base case where if s is empty then its automatically True
            return True
        i = 0 ## pointer for string s
        for char in t: ## iterate through characters in t
            if s[i] == char and i < len(s): ## check if char in s is equal to char in t and i is less than length of s to prevent out of bounds
                i = i + 1 ## move to the next char in s, if not than stay with same char in s and compare to next char in t
            if i == len(s): ## if you successfully loop through the entirety of t but didnt reach the end of s, then its False
                return True ## otherwise True
        return False