class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            temp=[]
            while i>0:
                temp.append(i%10)
                i=i//10
            temp.reverse()
            res.extend(temp)   
        return res
