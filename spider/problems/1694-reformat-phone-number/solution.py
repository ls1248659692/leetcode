class Solution:
    def reformatNumber(self, number: str) -> str:
        n = number.replace('-', '').replace(' ', '')
        ans = []
        for i in range(0, len(n), 3):
            ans.append(''.join(n[i: i + 3]))
            
        if len(ans) >= 2 and len(ans[-1]) == 1:
            ans[-1] = ans[-2][2] + ans[-1]
            ans[-2] = ans[-2][:2]
        return '-'.join(ans)