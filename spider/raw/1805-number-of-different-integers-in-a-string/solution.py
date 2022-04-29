class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tli =['']
        for ch in word:
            if not 0<=ord(ch)-ord('a')<26:
                tli[-1] += ch
            else:
                tli.append('')
        r = set([int(el) for el in tli if el])
        #print (r)

        return len(r)