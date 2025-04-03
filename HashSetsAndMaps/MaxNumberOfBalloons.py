## O(n) time O(1) space

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)  
        return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])




## were only concerned with number of bs, as, ls, os, and ns
## use hashmap to get the count of each char in text
## since we need 2 l's and 2 o's to get one balloon we need to do floor division by 2 
        # Ex: if text = 'balllooon' max 'balloon' you can make is still 2
## return min() because it ensures we can only form as many "balloon" words as the limiting character allows



