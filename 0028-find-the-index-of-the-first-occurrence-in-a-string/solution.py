class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i = haystack.index(needle)
            return i
        else:
            return -1