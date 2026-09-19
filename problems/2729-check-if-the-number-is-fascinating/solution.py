class Solution:
    def isFascinating(self, n: int) -> bool:
        res=f"{n}{2*n}{3*n}"
        if len(res)==9 and set(res)==set("123456789"):
            return True
        else:
            return False
