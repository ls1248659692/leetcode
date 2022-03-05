class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        # 26**n*a + 26**1*b
        for idx,value in enumerate(reversed(columnTitle)):
            # print(ord(i)-64)
            ans += (ord(value)-64)*26**idx
        return ans