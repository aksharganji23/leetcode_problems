class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_side(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            if l>=len(nums):
                return -1
            if nums[l]!=target:
                return -1
            return l
        def right_side(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if target>=nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            if r<0:
                return -1
            if nums[r]!=target:
                return -1
            return r
        a=left_side(nums,target)
        b=right_side(nums,target)
        ans=[]
        ans.append(a)
        ans.append(b)
        return ans
