## O(n+m) time O(1) space

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):  
        seen = Counter(magazine) 
        for char in ransomNote:
            if char in seen and seen[char] > 0:
                seen[char] = seen[char] - 1
            else:
                return False
        return True
    
## to see if all of ransomNote is in magazine: 
## Counter returns a hashmap of the count of each letter in the array magazine (seen)
## iterate through each char in ransomNote 
## Check if that char exists in your hash map (from magazine) and if the count is greater than 0
## if yes: decrease the count of that char by 1,
## if not: then its automatically false
## if you can go through all the chars, then its True