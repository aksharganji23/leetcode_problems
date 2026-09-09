class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        count=0
        x=0
        y=1000
        while(n-y>=0):
            count+=n-y
            y*=1000
            x+=1
        return count+x
