class Solution:
    def freqAlphabets(self, s: str) -> str:
        return ''.join([''.join([chr(ord('a')+int(d)-1) for d in el[:-2]])+chr(ord('j')+int(el[-2:])-10) for el in s.split('#')[:-1]]) + ''.join([chr(ord('a')+int(d)-1) for d in s.split('#')[-1]])