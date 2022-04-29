class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return set(list(ransomNote)).issubset(set(list(magazine))) and min([ magazine.count(ch)-ransomNote.count(ch) for ch in set(list(ransomNote))])>=0