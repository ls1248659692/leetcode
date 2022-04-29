class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(list(astr)))==len(astr)