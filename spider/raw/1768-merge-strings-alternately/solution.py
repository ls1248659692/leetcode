class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return (''.join([word1[i]+word2[i] for i in range(len(word1))])+word2[len(word1):])         if len(word1)<len(word2) else   (''.join([word1[i]+word2[i] for i in range(len(word2))])+word1[len(word2):])