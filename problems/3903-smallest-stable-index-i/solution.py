class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            l=max(nums[0:i+1])
            s=min(nums[i:len(nums)])
            diff=l-s
            if diff<=k:
                return i
        return -1
