class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=nums[0]
        for i in range(1,len(nums)):
            if i%2==0:
                ans+=nums[i]
        return ans
