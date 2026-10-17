class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character = set(s)
        if len(s) != len(t):
            return False
        for ch in character:
            if s.count(ch) != t.count(ch):
                return False
        return True