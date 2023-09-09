class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = gain[0]
        total = res
        for g in gain[1:]: 
            total += g
            print(total)
            if total > res:
                res = total
        if (res > 0): return res
        return 0