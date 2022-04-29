class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nu=[i*i for i in range(math.ceil(math.sqrt(c+1)))]
        snu = set(nu)
        for n in nu:
            if c-n in snu: return True
        return False