class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        s,sec=0,0
        for i in range(len(mat)):
            s+=mat[i][i]
            sec+=mat[i][len(mat)-1-i]
        ans=s+sec
        if len(mat)%2==1:
            ans-=mat[len(mat)//2][len(mat)//2]
        return ans
