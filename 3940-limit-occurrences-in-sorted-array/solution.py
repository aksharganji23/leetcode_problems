class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c=0
        i=j=0
        while j<=len(nums)-1:
            if nums[i]==nums[j]:
                if c<k:
                    c+=1
                    j+=1
                else:
                    nums.pop(j)
            else:
                i=j
                c=1
                j+=1      
        return nums