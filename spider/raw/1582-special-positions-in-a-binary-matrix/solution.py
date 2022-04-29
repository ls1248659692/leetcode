class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for r in range(n):
            if sum(mat[r]) == 1:
                col = mat[r].index(1)
                if sum(mat[i][col] for i in range(n)) == 1:
                    ans += 1
        return ans