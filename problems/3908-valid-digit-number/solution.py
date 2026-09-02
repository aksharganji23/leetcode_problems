class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        a=[]
        for i in range(len(str(n))):
            c=n%10
            a.append(c)
            n=n//10
        a=a[::-1]
        if x in a and a[0]!=x:
            return True
        else:
            return False
