## O(n*m) time O(1) space
class Solution(object):
    def longestCommonPrefix(self, strs):
        for i, char in enumerate(strs[0]): ## iterate over the indexes and characters of the first word in strs
            for word in strs[1:]: ## also iterate over the rest of the words in strs
                if i < len(word): ## checking if the first word is bigger/smaller than the other words
                    if char == word[i]: ## is the char in the first word equal to the current word at the current index?
                        continue ## if yes, move to the next word in strs
                    else:
                        return strs[0][:i] ## if not return all the chars in the first word of strs up until that index
                else: 
                    return strs[0][:i] ## if word is bigger than the first word then return all the chars in first word up till i 
        return strs[0] ## returning common chars