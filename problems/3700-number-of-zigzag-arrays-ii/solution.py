class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        # Initial state vector
        vec = [1] * (m - 1) + [0] + [0] + [1] * (m - 1)
        size = 2 * m
        # Transition matrix
        M = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i + 1, m):
                M[i][m + j] = 1
            for j in range(i):
                M[m + i][j] = 1
        def mat_mul(A, B):
            n = len(A)
            p = len(B[0])
            m2 = len(B)
            res = [[0] * p for _ in range(n)]
            for i in range(n):
                for k in range(m2):
                    if A[i][k]:
                        a = A[i][k]
                        for j in range(p):
                            res[i][j] = (res[i][j] + a * B[k][j]) % MOD
            return res
        def mat_pow(mat, power):
            size = len(mat)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            while power:
                if power & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return res
        if n == 1:
            return m
        P = mat_pow(M, n - 1)
        vec_col = [[x] for x in vec]
        ans_vec = mat_mul(P, vec_col)
        return sum(row[0] for row in ans_vec) % MOD
