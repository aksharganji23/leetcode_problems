class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici={}
        count=0
        for i in range(len(nums)):
            if nums[i] in dici:
                dici[nums[i]]+=1
            else:
                dici[nums[i]]=1
        for key,values in dici.items():
            if values>=2:
                count+=1
        if count!=0:
            return True
        else:
            return False
