class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        mini=float("inf")
        for r in range(len(nums)):
            if r-l+1==k:
                temp=nums[r]-nums[l]
                mini=min(mini,temp)
                l+=1
        return mini
