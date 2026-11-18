class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        t=int(c**(0.5))
        i=0
        while i<=t:
            k=i**2+t**2
            if k==c:
                return True
            elif k<c:
                i+=1
            elif k>c:
                t-=1
        return False