class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        tli= [s[i:i+3] for i in range(len(s)-2) if len(set(list(s[i:i+3])))==3]
        print(tli)
        return len(tli)