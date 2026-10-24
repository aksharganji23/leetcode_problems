class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        d={}
        for n in nums2:
            while stack and n>stack[-1]:
                t=stack.pop()
                d[t]=n
            stack.append(n)
        
        while len(stack)!=0:
            t=stack.pop()
            d[t]=-1


        res=[]
        for n in nums1:
            res.append(d.get(n,-1))

        return res