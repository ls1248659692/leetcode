class Solution:
    def minimumSum(self, num: int) -> int:
        a,b,c,d=sorted(list(str(num)))
        return int(a)*10+int(b)*10+int(c)+int(d)