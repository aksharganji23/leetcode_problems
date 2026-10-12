class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r  
        start, end = 0, 1
        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):  
                if r - l > end - start:
                    start, end = l, r
        return s[start:end]
