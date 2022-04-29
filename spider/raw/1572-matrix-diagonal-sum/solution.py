class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        m = 0 
        while m < len(mat):
            ans += mat[m][m] + mat[m][-m-1]
            m += 1
        if len(mat) % 2 == 1:
            ans -= mat[len(mat)//2][len(mat)//2]
        return ans