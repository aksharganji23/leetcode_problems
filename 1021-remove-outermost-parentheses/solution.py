class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        ans = ""
        for ch in s:
            if ch=='(':
                if c>0:
                    ans+=ch
                c+=1
            elif ch==')':
                c-=1
                if c>0:
                    ans+=ch
        return ans