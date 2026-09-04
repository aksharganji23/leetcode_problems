class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=min(nums1)
        for i in nums1:
            if m%2==0 and i%2!=0:
                return False
        return True
