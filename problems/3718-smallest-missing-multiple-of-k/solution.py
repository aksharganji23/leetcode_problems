class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=1
        while True:
            if k*n not in nums:
                return k*n
            n+=1
