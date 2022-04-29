class Solution:
    def longestPalindrome(self, s: str) -> int:
        tli = [s.count(ch) for ch in set(list(s))]
        print(tli)
        return (1 if sum([el %2 for el in tli])>0 else 0) + sum([el//2 for el in tli])*2