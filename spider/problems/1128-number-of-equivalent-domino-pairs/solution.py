class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        cnt = 0
        dic = {}
        for a, b in dominoes:
            k = str(a) + str(b) if a > b else str(b) + str(a)
            dic[k] = dic.get(k, 0) + 1
        for k in dic:
            v = dic[k]
            if v > 1:
                cnt += (v * (v - 1)) // 2
        return cnt
