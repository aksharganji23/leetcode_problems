class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1
        for key,values in count.items():
            if values>1:
                return key
