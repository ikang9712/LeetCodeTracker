class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = address.split(".")
        res = addr[0]
        for i in addr[1:]:
            res = res + "[.]"  + i
        return res