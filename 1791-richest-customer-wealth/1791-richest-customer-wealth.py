class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            if sum(account) > max:
                max = sum(account)
        return max