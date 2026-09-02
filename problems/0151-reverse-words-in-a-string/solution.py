class Solution:
    def reverseWords(self, s: str) -> str:
        rev=[]
        for i in s:
            words=s.split()
        rev=words[::-1]
        print(rev)
        r=" ".join(rev)
        return r
