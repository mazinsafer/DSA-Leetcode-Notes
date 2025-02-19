def containsDuplicate(self, nums): ## Bruce Force solution O(n^2)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True
        return False

def containsDuplicate(self, nums): ## Hashset is O(n) space and time
        new = set()
        for i in nums:
            if i in new:
                return True
            new.add(i)
        return False


