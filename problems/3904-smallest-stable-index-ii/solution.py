class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefmax=[0]*len(nums)
        suffmin=[0]*len(nums)
        prefmax[0]=nums[0]
        for i in range(1,len(nums)):
            prefmax[i]=max(prefmax[i-1],nums[i])
        suffmin[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffmin[i]=min(suffmin[i+1],nums[i])
        for i in range(len(nums)):
            score=prefmax[i]-suffmin[i]
            if score<=k:
                return i
        return -1
