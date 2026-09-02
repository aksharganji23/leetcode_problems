class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        ls=0
        for i in range(len(nums)):
            rs= total_sum - ls - nums[i]
            if rs==ls:
                return i
            ls+=nums[i]
        return -1
