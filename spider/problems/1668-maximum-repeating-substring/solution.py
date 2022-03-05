class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        se,wd,k = sequence,word,100//len(word)
        if wd not in se:return 0
        while k>0 and wd*k not in se:
            k-=1
        return k        