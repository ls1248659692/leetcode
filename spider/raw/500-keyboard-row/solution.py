class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [wd for wd in words  if set(list(wd.lower())).issubset(set(list("qwertyuiop"))) or set(list(wd.lower())).issubset(set(list("asdfghjkl"))) or set(list(wd.lower())).issubset(set(list("zxcvbnm")))]