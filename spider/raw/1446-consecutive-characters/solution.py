class Solution:
    def maxPower(self, s: str) -> int:
        tli = [s[0]]
        for ch in s[1:]:
            if ch ==tli[-1][-1]:tli[-1] +=ch
            else: tli.append(ch)
        return max(len(el) for el in tli)