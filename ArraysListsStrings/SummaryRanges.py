## My Brute Force solution  O(nlogn) time O(n) space on average
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        j = 1
        if not nums:
            return result
        start = nums[0]
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if start + j in nums:
                    j = j + 1
                elif start + j not in nums:
                    stop = nums[i]
                    if start == stop:
                         result.append(f"{start}") 
                    else:
                          result.append(f"{start}->{stop}")
                    j = 1
                    stop = 0
                    start = nums[i+1]
            else:
                stop = nums[i]
                if stop == start:
                    result.append(f"{stop}")
                else:
                    result.append(f"{start}->{stop}")
                    return result
        return result
    

## More optimal O(n) time and space

from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    result = []  ## nums[n-1] is essentially the stop variable in this solution
    if not nums:
        return result
    start = nums[0]  ## starting from the first element in nums
    for i in range(1, len(nums)):  ## loop through the rest of the elements
        if nums[i] != nums[i - 1] + 1:  ## if nums[i] is not the consecutive number of the one before it (checking for a break)
            if start == nums[i - 1]: ## if start is the same as the number before nums[i] (stop)
                result.append(f"{start}") ## then just append that number
            else:  ## if they are different
                result.append(f"{start}->{nums[i - 1]}") #append start and stop
            start = nums[i]  # Update new range start
        else: 
            continue ## if there not consecutive just move to the next iteration

    # Append the last range
    if start == nums[-1]:
        result.append(f"{start}")
    else:
        result.append(f"{start}->{nums[-1]}")
    
    return result
