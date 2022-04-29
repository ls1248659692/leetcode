class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        t1= [w2 for w2 in words1 if words1.count(w2)==1]
        t2 = [w2 for w2 in words2 if words2.count(w2)==1]
        return len([wd1 for wd1 in t1 if wd1 in t2])