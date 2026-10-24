class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        nines=sum//9
        rem=sum%9
        ans="9"*nines
        if rem:
            ans+=str(rem)
        ans+="0"*(num-len(ans)) 
        return ans