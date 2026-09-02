class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_s=""
        for ch in s:
            if ch.isalnum():
                s_s+=ch.lower()
        return s_s==s_s[::-1]
