class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        a=[]
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,values in freq.items():
            a.append(values)
        for i in a:
            if a.count(i)!=1:
                return False
        return True
