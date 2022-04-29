class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(wd).issubset(set(allowed))  for wd in words )