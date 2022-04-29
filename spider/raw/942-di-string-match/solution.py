class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res=[0]
        for c in s:
            if c=='I': res.append(max(res)+1)
            else: res.append(min(res)-1)
        r =[el-min(res) for el in res]
        print(r)
        return r
        