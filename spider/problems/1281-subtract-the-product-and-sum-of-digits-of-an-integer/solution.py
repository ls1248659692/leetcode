class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        add= 0
        multi = 1
        for i in n:
            add = int(i) + add
        for j in n:
            multi = int(j) * multi
        return multi-add