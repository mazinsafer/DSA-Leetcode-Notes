#O(n) time O(1) space
## Two pointers is perferred because using a hashmap would be O(n) space

class Solution(object):
    def twoSum(self, numbers, target):
        right = len(numbers) - 1
        left = 0
        while right > left:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else: 
                return [left+1, right+1]
            

## inialize left and right pointers
## while right > left
## since numbers is sorted, you can manipulate the pointers based on their sum to reach the target val
## if the sum of the left val and right val is less than the target, decrease the right pointer by 1
## if the sum of left val and the right val is more than the target, increase the left pointer by 1
## return +1 because the problem says return indicies + 1
