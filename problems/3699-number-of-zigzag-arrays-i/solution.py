class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        up = [0] * (m + 1)
        down = [0] * (m + 1)
        for y in range(1, m + 1):
            up[y] = y - 1
            down[y] = m - y
        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            for i in range(1, m + 1):
                pref_down[i] = (pref_down[i - 1] + down[i]) % MOD
            suff_up = [0] * (m + 2)
            for i in range(m, 0, -1):
                suff_up[i] = (suff_up[i + 1] + up[i]) % MOD
            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)
            for y in range(1, m + 1):
                new_up[y] = pref_down[y - 1]      # x < y
                new_down[y] = suff_up[y + 1]      # x > y
            up, down = new_up, new_down
        ans = (sum(up) + sum(down)) % MOD
        return ans
