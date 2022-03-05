class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return   len([wd for wd in text.split() if not set(list(wd)).intersection(set(list(brokenLetters)))])