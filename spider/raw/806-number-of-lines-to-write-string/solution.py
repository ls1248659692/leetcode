class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line,cum,n=1,0,0
        
        for ch in s:
            n=widths[ord(ch)-ord('a')]
            if cum+ n>100: line,cum =line+1,n
            else: cum = cum+n
        return line,cum