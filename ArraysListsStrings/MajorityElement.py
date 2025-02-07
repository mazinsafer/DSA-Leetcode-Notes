def majorityElement(self, nums):
        candidate = None
        counter = 0
        n = len(nums)
        for i in nums:
            if counter == 0:
                candidate = i
            if candidate != i:
                counter = counter - 1
            if candidate == i:
                counter = counter + 1
        return candidate