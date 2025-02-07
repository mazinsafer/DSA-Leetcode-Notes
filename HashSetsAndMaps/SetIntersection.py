## Brute force approach, inefficient with O(n*m)

def intersection(self, nums1, nums2):
        nums4 = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums4.add(nums1[i])
        return list(nums4)

## Better solution is to use set intersection

def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))