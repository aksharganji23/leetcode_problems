class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=""
        maxi=0
        count=0
        for i in s:
            if i not in a:
                a+=i
                count+=1
                maxi=max(maxi,count)
            elif a[-1]==i:
                maxi=max(maxi,count)
                a=i
                count=1
            else:
                maxi=max(maxi,count)
                v=a.index(i)
                a=a[v+1::]
                a+=i
                count=(len(a))
        return maxi        

