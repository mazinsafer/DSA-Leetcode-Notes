## O(nlogn) time O(1) space
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        min_bananas = right + 1
        while left <= right:
            m = (left + right) // 2
            hrs = 0
            for pile in piles:
                hrs = hrs + (-(-pile // m)) ## ceiling division
            if hrs <= h:
                if m <= min_bananas:
                    min_bananas = m
                    right = m - 1
                else:
                    left = m + 1
            else:
                left = m + 1


        return min_bananas
    

## Left pointer starting at 1, right pointer starting at the max of piles
    ## Because k can only be 1-max(piles)
## initialize a min_bananas (k value) value so we can compare and update
## reset the number of hrs for every k value (hrs = 0)
## add up the amount of hours for that k in the for loop
## if hrs is less than h (valid)
    ## then check if current k is less than the current min_bananas, if it is update it.
    ## also move right over to the left because we want the smallest possible value
    ## if k is bigger than current min_bananas move k to the right
    
    ## if hrs is bigger than h, k is too small so move k to the right

## return min_bananas