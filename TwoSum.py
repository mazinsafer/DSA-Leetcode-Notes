## initialize a dictionary 
## enumerate for loop to iterate over the index and actual num in nums
## calculate the complement which is target - num
## check if complement is in the dictionary 
    ##if yes: return the stored index and current index
    ##if no: store num in dictionary
## if no is soultuion is found return an empty list


def twoSum(self, nums, target):
    my_dict = {}  ## Create dictionary
    for i, num in enumerate(nums):  ##  Loop through list
        complement = target - num  ## Find complement
        if complement in my_dict:  ## Check if complement exists
            return [my_dict[complement], i]  ## Return indexes
        my_dict[num] = i  ## Store number and index
    return []  ## Return empty if no solution
