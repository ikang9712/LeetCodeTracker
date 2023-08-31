from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in Counter(nums1):
            if num in Counter(nums2):
                res.append(num)
        return res
