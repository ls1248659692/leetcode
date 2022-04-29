class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return [wd for wd in words if wd==wd[::-1]][0] if [wd for wd in words if wd==wd[::-1]] else ''