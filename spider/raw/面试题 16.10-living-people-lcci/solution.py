class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        i = list(range(1900,2001))
        cnt = {}
        for i in range(len(birth)):
            for year in range(birth[i],death[i]+1):
                cnt[year] = cnt.get(year,0)+1
        return sorted([(i,cnt[i]) for i in cnt],key = lambda x:(x[1],-x[0]))[-1][0]