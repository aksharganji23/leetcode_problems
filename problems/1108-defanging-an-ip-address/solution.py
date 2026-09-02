class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=""
        for num in address:
            if num == ".":
                res+= "[.]"
            else:
                res+=num
        return res
