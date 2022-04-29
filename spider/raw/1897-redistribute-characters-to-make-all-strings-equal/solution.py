class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wds= ''.join(words)
        return len([c for c in set(list(wds)) if wds.count(c)%len(words)!=0])==0