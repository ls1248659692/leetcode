class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        se,sw = sentence.split(),searchWord
        for i in range(len(se)):
            if len(se[i])>=len(sw) and se[i][:len(sw)] ==sw: return i+1
        return -1