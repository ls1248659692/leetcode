class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx = 0
        cnt = 0
        for i in word:
            idxn =keyboard.index(i)
            cnt += abs(idxn-idx)
            idx = idxn
        return cnt