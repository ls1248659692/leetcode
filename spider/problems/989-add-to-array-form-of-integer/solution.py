class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = ''
        for i in num:
            ans += str(i)
        return [int(i) for i in str(int(ans)+k)]