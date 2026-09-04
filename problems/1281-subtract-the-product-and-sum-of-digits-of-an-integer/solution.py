class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while n>0:
            d=n%10
            s,p=s+d,p*d
            n//=10
        return p-s
