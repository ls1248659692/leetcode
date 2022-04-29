class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sn = sorted(score,reverse=True)
        tn = ['Gold Medal','Silver Medal','Bronze Medal']+ [str(e) for e in range(4,len(sn)+1)]
        return [tn[sn.index(n)] for n in score]