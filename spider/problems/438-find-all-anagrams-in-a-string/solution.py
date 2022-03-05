class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []
        sp = ''.join(sorted(list(p)))
        return [i for i in range(len(s)-len(p)+1) if ''.join(sorted(list(s[i:i+len(p)]))) == sp]