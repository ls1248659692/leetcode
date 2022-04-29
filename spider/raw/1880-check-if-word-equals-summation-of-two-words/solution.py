class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d= dict(zip(list('abcdefghij'),list('0123456789')))
        return int(''.join([d[ch] for ch in firstWord])) +int(''.join([d[ch] for ch in secondWord]))==int(''.join([d[ch] for ch in targetWord]))