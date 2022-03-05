class Solution:
    def minTimeToType(self, word: str) -> int:
        return len(word) + min(ord(word[0])-ord('a'), 26+ord('a')-ord(word[0]))  + sum ([min(abs(ord(word[ii])-ord(word[ii-1])),26-abs(ord(word[ii])-ord(word[ii-1]))) for ii in range(1,len(word))])