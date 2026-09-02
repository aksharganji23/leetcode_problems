class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for key,value in count.items():
            if value>(n/2):
                return key
