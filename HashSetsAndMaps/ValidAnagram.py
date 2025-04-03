## O(n) time and space

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        seen = Counter(s)
        teen = Counter(t)
        for char, count in seen.items():
            if seen[char] == teen[char]:
                continue
            else:
                return False
        return True

## anagram: you can rearrange the letters of another word and create another word
## first, if the lengths of the two strings are different you know there not anagrams
## use Counter to create hashmaps of the counts of the chars in s and t
## iterate through char:count in seen
## if the count of the char in seen is the same as teen: go to the next char:count pair
## if not: return False 
## if you are able to iterate through all the items in seen return True