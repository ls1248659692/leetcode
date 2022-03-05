class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(sentence)==set(list('abcdefghijklmnopqrstuvwxyz'))