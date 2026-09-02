class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        ans=[]
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        for key,values in freq.items():
            if values==1:
                ans.append(key)
        return sum(ans)
