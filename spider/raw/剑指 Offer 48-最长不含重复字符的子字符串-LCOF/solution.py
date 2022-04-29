class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        rli = [(i,i+1) for i in range(len(s))]
        while rli:
            rla= rli
            rli = [(i-1,j) for i,j in rli if i>=1 and s[i-1]not in s[i:j]]
        return rla[0][1]-rla[0][0]