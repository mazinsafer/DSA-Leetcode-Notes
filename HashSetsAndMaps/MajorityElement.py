## O(n) time and space

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        my_dict = Counter(nums)
        candidate = 0
        curr_max = 0
        for key, count in my_dict.items():
            if count > curr_max:
                candidate = key
                curr_max = count
        return candidate

## O(n) time O(1) space

def majorityElement(self, nums):
        candidate = None
        counter = 0
        for num in nums:
            if counter == 0:
                candidate = num
            if candidate != num:
                counter = counter - 1
            if candidate == num:
                counter = counter + 1
        return candidate