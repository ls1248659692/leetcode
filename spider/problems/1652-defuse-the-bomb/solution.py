class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if not k:
            return ans
        for i in range(n):
            for j in range(abs(k)):
                ans[i] += code[(i+j+1)%n] if k > 0 else code[(i-j-1)%n]
        return ans
