class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        i=0
        while i<len(s):
            if freq[s[i]]==1:
                return i
            i+=1
        return -1
