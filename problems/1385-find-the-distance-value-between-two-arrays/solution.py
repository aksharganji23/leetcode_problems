class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=0
        for i in range(len(arr1)):
            swapped=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    swapped+=1
            if swapped==len(arr2):
                ans+=1
        return ans
