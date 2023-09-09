class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = nums[0]
        res = [c]
        for num in nums[1:]:
            res.append(c+num)
            c = c+num
        return res