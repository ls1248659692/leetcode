class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == './':
                continue
            if i == '../' :
                if ans ==0:
                    continue
                else:
                    ans -= 1
            else:
                ans += 1
        return ans if ans>=0 else 0