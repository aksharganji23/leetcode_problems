class Solution:
    def reverse(self, x: int) -> int:
        s = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return s if -2**31 <= s <= 2**31 - 1 else 0
