class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        s = str(n)
        res = ""
        for c in s:
            if c not in dic:
                return False
            res = dic[c] + res
        return res != s
