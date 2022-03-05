class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum([ 1 for ss in s[:len(s)//2] if ss in 'AEIOUaeiou'])==sum([ 1 for ss in s[len(s)//2:]if ss in 'AEIOUaeiou'])