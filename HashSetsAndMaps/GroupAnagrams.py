from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)

        return anagrams_dict.values()

        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
# Initialize a defaultdict where each key will map to a list of anagrams
# Iterate through each word in the input list 'strs'
# Initialize a count list of size 26 (for each letter in the alphabet, from 'a' to 'z')
# This list will store the frequency of each letter in the word
#  Iterate through each character in the word
## Use ord(char) to get the ASCII value of the character
 #Subtract ord('a') to get the index corresponding to the character's position in the alphabet
# Increment the count at the corresponding index for the character
# Convert the 'count' list into a tuple so it can be used as a dictionary key
# Using a tuple because lists are not hashable, but tuples are
# The tuple of character counts will be unique for each set of anagrams
## Add the word to the dictionary under the key created by its character counts (anagram_key)
# If this key doesn't exist, defaultdict automatically creates a new list for it
# Convert the values (groups of anagrams) in the dictionary into a list and return it