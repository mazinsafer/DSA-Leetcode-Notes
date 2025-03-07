## Python specific: O(n) time and space
class Solution(object):
    def mergeAlternately(self, word1, word2): 
        newword = "" ## create new string
        while word1 or word2:  ## while word1 or word2 has characters
            if word1:
                newword += word1[0]  # Take first letter
                word1 = word1[1:]  # Remove first letter
            if word2:
                newword += word2[0]  # Take first letter
                word2 = word2[1:]  # Remove first letter
        return newword
    
# O(n) time and space
class Solution(object):
    def mergeAlternately(self, word1, word2): 
        newword = "" ## create new string
        i = 0    ## word1 and word2 pointers to add indexes to newword
        j = 0       
        while i < len(word1) or j < len(word2): # while i or j dont exceed the lengths of one of the words
            if i < len(word1): ## if i/j is less then length of word1/2
                newword = newword + word1[i]  ## add the first character of word1/2 to newword
                i = i + 1 ## increment i/j to add the next character of word1/2 in the next iteration
            if j < len(word2):
                newword = newword + word2[j]   
                j = j + 1
        return newword 