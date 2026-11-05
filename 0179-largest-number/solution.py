class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=[]
        for i in nums:
            res.append(str(i))
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                if res[i]+res[j]<res[j]+res[i]:
                    res[i],res[j]=res[j],res[i]
        return str(int("".join(res)))