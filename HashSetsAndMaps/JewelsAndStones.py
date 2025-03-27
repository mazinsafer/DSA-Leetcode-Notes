##O(n+m) time O(n) space


class Solution(object):
    def numJewelsInStones(self, jewels, stones):   
        j = set(jewels)
        counter = 0  
        for stone in stones:
            if stone in j:
                counter = counter + 1
        return counter
    
    ## use hashset to remove duplicates in jewels
    ## counter to keep track of the number stones that are also jewels
    ## iterate through stones