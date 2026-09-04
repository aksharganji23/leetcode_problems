class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a,s,p=n,0,1
        while n:
            d=n%10
            s,p=s+d,p*d
            n//=10
        k=s+p
        if a%k==0:
            return True
        else:
            return False
