class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        for keys,values in count.items():
            if values==1:
                return keys
