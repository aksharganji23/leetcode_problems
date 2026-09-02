class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        # Pass 1: Calculate the total length of the final string
        for c in s:
            if c == "*":
                m = max(0, m - 1)
            elif c == "#":
                m <<= 1  # Equivalent to m = m * 2
            elif c != "%":
                m += 1   # Regular lowercase English letter
                
        # If k is out of bounds of the final string length
        if k >= m:
            return "."
            
        # Pass 2: Backtrack from right to left to locate the character
        for c in reversed(s):
            if c == "*":
                m += 1
            elif c == "#":
                m //= 2
                if k >= m:
                    k -= m
            elif c == "%":
                k = m - 1 - k
            else:
                m -= 1
                if k == m:
                    return c
